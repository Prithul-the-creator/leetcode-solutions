# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        result = float("-inf")
        def dfs(node):
            nonlocal result
            if not node:
                return 0
            
            a = dfs(node.left)
            b = dfs(node.right)
            result = max(result, max(a,0) + max(b,0) + node.val)
            
            return max(0, a, b) + node.val
        dfs(root)
        return result


        
