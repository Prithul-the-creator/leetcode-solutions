# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        results = []
        def bfs(node, level):

            if not node:
                return
            
            if len(results) <= level:
                results.append([])
            
            results[level].append(node.val)
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
        
        bfs(root, 0)
        return [result[-1] for result in results]
        
