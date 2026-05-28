# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        hashmap = {}


        curr = head
        index = 0
        while curr:
            hashmap[index] = curr
            curr = curr.next
            index += 1
        index -= 1

        if index - n == -1:
            head = head.next
            return head

        node = hashmap[index - n]
        node.next = node.next.next
        return head

        

        



