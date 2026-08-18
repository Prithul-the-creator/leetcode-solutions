# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        visited = set()
        last = None
        def bfs(node, current):  
            nonlocal last
            if node in visited:
                last = node
            visited.add(node)
            if node.val == current.val:
                return
            if node.val > current.val:
                bfs(node.left, current)
            else:
                bfs(node.right, current)
            
        bfs(root, p)
        bfs(root, q)
        return last




        
