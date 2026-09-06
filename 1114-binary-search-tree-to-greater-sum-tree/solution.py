# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        current = 0
        def reverse(node):
            nonlocal current
            if not node:
                return
            
            reverse(node.right)
            current += node.val
            node.val = current
            reverse(node.left)
        reverse(root)
        return root
        
