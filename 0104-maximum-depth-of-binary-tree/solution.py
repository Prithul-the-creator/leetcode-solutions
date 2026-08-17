# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        result = 1
        def dfs(node, count):
            nonlocal result
            if not node:
                return
            if not node.right and not node.left:
                result = max(result, count)
                return
            
            dfs(node.left, count + 1)
            dfs(node.right, count + 1)
        
        dfs(root, 1)
        return result
            

            





        
