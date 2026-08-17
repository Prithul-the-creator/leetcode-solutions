# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        result = 0
        def dfs(node, count):
            nonlocal result
            if not node:
                return 0
            
            a = dfs(node.left, count + 1)
            b = dfs(node.right, count + 1)
            result = max(result, a + b)
            return max(a, b) + 1
        
        dfs(root, 0)
        return result

        

