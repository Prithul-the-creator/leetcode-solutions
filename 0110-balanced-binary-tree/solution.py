# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        result = True
        def dfs(node):

            nonlocal result
            if not node:
                return 0

            a = dfs(node.left)
            b = dfs(node.right)
            if abs(a - b) > 1:
                result = False

            return 1 + max(a, b)

        dfs(root)
        return result
        
