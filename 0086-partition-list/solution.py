# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:


        if not head:
            return

        result = ListNode(0)
        tail = result

        extra = ListNode(0)
        extratail = extra

        curr = head
        

        while curr:


            if curr.val < x:

                tail.next = curr
                tail = tail.next
            
            else: 

                extratail.next = curr
                extratail = extratail.next
                
            
            curr = curr.next

        extratail.next = None

        tail.next = extra.next
        return result.next
        











        
