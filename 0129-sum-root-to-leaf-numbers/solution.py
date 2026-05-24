# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:


        result = 0

        def dfs(node, currentsum):
            nonlocal result
            if not node:
                return
            if not node.right and not node.left:
                result += int(currentsum + str(node.val))
                return
            

            dfs(node.left, currentsum + str(node.val))
            dfs(node.right, currentsum + str(node.val))

        dfs(root, "")

        return result





        
