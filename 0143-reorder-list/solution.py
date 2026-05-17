# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        counter = {}
        curr = head
        count = 0

        while curr:
            counter[count] = curr
            curr = curr.next
            count += 1

   


        i = 0
        result = ListNode(0)
        resultTail = result

        for i in range(count // 2):
            resultTail.next = counter[i]
            resultTail = resultTail.next
            resultTail.next = counter[count - i - 1]
            resultTail = resultTail.next

        if count % 2 == 1:
            resultTail.next = counter[count//2]
            resultTail = resultTail.next
        resultTail.next = None

        return result.next


