# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        curr = head
        prev = head
        curr = curr.next
        index = 1
        critical = []

        while curr:

            if curr.next == None:
                curr = curr.next
                continue
            
            if (prev.val < curr.val and curr.val > curr.next.val) or (prev.val > curr.val and curr.val < curr.next.val):
                critical.append(index)
            
            curr = curr.next
            prev = prev.next
            index += 1
        
        if len(critical) < 2:
            return [-1, -1]
        mindistance = float("inf")
        for i in range(len(critical) - 1):
            mindistance = min(mindistance, critical[i + 1] - critical[i])

        return [mindistance, critical[-1] - critical[0]]




            

            

        
