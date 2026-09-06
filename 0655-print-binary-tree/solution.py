# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        traversal = []

        def traverse(node):

            if not node:
                traversal.append("N")
                return -1
            
            traversal.append(node.val)
            a = traverse(node.left)
            b = traverse(node.right)
            return max(a, b) + 1

        height = traverse(root)
        rows = height + 1
        cols = 2 ** (height + 1) - 1

        grid = [[""]*cols for i in range(rows)]
        index = 0
        def populate_matrix(i, j):
            nonlocal index
            if traversal[index] == "N":
                return
            
            grid[i][j] = str(traversal[index])
            index += 1
            populate_matrix(i + 1, j - 2 ** (height - i - 1))
            index += 1
            populate_matrix(i + 1, j + 2 ** (height - i - 1))
            
        populate_matrix(0, cols // 2)
        return grid

            


        

        
