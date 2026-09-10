# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        result = 0
        def dfs(node):
            nonlocal result
            if not node:
                #return current_sum, num of nodes in subtree
                return 0, 0
            
            asum, acount = dfs(node.left)
            bsum, bcount = dfs(node.right)
            average = (asum + bsum + node.val) // (acount + bcount + 1)
            #print(average)
            if average == node.val:
                result += 1
            return asum + bsum + node.val, acount + bcount + 1
        dfs(root)
        return result




            

        
