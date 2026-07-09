# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        


        result = TreeNode(max(nums))

        def recurse(array, node):
            nonlocal result

            indexOfMaximum = array.index(max(array))

            leftarray = array[0: indexOfMaximum]
            rightarray = array[indexOfMaximum + 1: ]

            if leftarray:
                leftnode = TreeNode(max(leftarray))
                node.left = leftnode
                recurse(leftarray, leftnode)

            if rightarray:
                rightnode = TreeNode(max(rightarray))
                node.right = rightnode
                recurse(rightarray, rightnode)
        
        recurse(nums, result)
        return result

