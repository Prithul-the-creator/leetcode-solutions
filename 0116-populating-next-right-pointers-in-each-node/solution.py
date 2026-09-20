"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':


        nodes = []
        def dfs(node, level):

            if not node:
                return
            
            if level >= len(nodes):
                nodes.append([])
            
            nodes[level].append(node)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)



        dfs(root, 0)
        for level in nodes:
            for i in range(len(level)):
                if i == len(level) - 1:
                    level[i].next = None
                    continue
                level[i].next = level[i + 1]
        return root
                





        
