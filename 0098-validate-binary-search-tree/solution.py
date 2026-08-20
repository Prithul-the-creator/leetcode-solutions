# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.result = True
        self.smallest = float("-inf")
        def dfs(node):

            if not node:
                return
                
            dfs(node.left)
            if node.val <= self.smallest:
                self.result = False
                return
            self.smallest = node.val
            dfs(node.right)

        
        dfs(root)
        return self.result
        

            
