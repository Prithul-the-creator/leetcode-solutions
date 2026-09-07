# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        result, found = None, False

        def dfs(node):
            
            if not node:
                return None
            
            if node.val == q.val or node.val == p.val:
                return node
            a = dfs(node.left)
            b = dfs(node.right)
            if a and b:
                return node
            if a: return a
            if b: return b
            return None
            
        return dfs(root)
        
