# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverseKnodes(head, count):
            nonlocal i, result
            prev = None
            curr = head

            while curr and count > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count -= 1

            head.next = curr
            return prev, head
        


        start = head
        end = head
        result = ListNode(0)
        tail = result

        i = 1

        while end:

            if i % 2 == 0:

                nextNode = end.next
                first, last = reverseKnodes(start, 2)
                tail.next = first
                tail = last
                last.next = nextNode
                start = nextNode
                end = nextNode

            else:
                #print(end.val)
                end = end.next

            i += 1
        
        if i == 2:
            return head
            
        return result.next

        
