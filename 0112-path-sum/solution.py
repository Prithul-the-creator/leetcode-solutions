# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        sums = []

        def recurse(node, currSum):

            if not node:
                return 0
        
            if not node.left and not node.right:
                currSum += node.val
                sums.append(currSum)
                            

            recurse(node.left, currSum + node.val)
            recurse(node.right, currSum + node.val)

        recurse(root, 0)
        return targetSum in sums
