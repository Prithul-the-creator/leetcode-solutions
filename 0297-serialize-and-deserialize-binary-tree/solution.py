# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        
        result = []
        def dfs(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        result = " ".join(result)
        
        return result
            

    def deserialize(self, data):
        index = 0
        data = data.split(" ")
        def dfs():
            nonlocal index
            if index >= len(data) or data[index] == "N":
                return None
            
            current = TreeNode(data[index])
            index += 1
            current.left = dfs()
            index += 1
            current.right = dfs()

            return current
        return dfs()
            
            
            

            


        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
