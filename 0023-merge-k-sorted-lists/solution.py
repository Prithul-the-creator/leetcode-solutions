# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        for head in lists:
            curr = head
            while curr:
                
                heapq.heappush(heap, curr.val)
                curr = curr.next
        
        result = ListNode(0)
        tail = result

        while heap:

            node = ListNode(heapq.heappop(heap))
            tail.next = node
            tail = node
        
        return result.next

            
            

            



        


        
