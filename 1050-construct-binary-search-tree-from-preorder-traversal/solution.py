# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        index = 1
        root = TreeNode(preorder[0])
        def dfs(node, left, right):
            nonlocal index
            if index >= len(preorder):
                return
            if preorder[index] < node.val and preorder[index] > left:
                node.left = TreeNode(preorder[index])
                index += 1
                dfs(node.left, left, node.val)
            if index >= len(preorder):
                return
            if preorder[index] > node.val and preorder[index] < right:
                node.right = TreeNode(preorder[index])
                index += 1
                dfs(node.right, node.val, right)
        dfs(root, float("-inf"), float("inf"))
        return root
            



        
