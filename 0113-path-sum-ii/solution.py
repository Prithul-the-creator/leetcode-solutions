# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:

        result = []
        def dfs(node, current, path):

            if not node:
                return
            
            path.append(node.val)
            current += node.val
            if not node.left and not node.right:
                if current == targetSum:
                    result.append(path[:])
            dfs(node.left, current, path)
            dfs(node.right, current, path)
            path.pop()
            current -= node.val
            
        
        dfs(root, 0, [])
        return result
            
            


        
