# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        result1 = 0
        digit = 1

        curr = l1

        while curr:
            
            result1 += curr.val * digit
            curr = curr.next
            digit *= 10
        
        result2 = 0
        digit = 1

        curr = l2

        while curr:
            
            result2 += curr.val * digit
            curr = curr.next
            digit *= 10
        
        total = result1 + result2
        if total == 0:
            return ListNode(0)
        
        result = ListNode(0)
    
        while total > 0:
            
            curr = total % 10
            total //= 10
        

            currnode = result
            while currnode.next:

                currnode = currnode.next
            
            currnode.next = ListNode(curr)
        
        return result.next






