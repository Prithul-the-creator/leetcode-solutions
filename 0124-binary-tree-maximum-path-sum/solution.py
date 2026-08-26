# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        result = root.val
        def dfs(node):
            nonlocal result
            if not node:
                return 0
            
            a = dfs(node.left)
            b = dfs(node.right)
            
            result = max(result, node.val + max(a, 0) + max(b, 0))
            return node.val + max(0, a, b)
        
        dfs(root)
        return result

