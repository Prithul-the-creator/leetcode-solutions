# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        result = True
        def dfs(node1, node2):
            nonlocal result
            if node1 and node2:
                if node1.val != node2.val:
                    result = False
                    return
            elif node1 != node2:
                result = False
                return
            else:
                return
            

            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)
        
        dfs(p, q)
        return result
        
