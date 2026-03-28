# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # performing preorder traversal
        self.string = ''
        # serialization should add delimiterss
        def preorder(root):
            if not root:
                return ''
            self.string += str(root.val) + ','
            preorder(root.left)
            preorder(root.right)
            return self.string
        return preorder(root)[:-1]

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if (not data):
            return None
        self.idx = 0
        arr = data.split(',')
        print(arr)
        def constructTree(data, lower_limit, upper_limit):
            if (self.idx) == len(data):
                return None
            val = int(data[self.idx])
            if not (lower_limit < val < upper_limit):
                return None
            root = TreeNode(val)
            self.idx += 1
            root.left = constructTree(data, lower_limit, val)
            root.right = constructTree(data, val, upper_limit)
            return root

        return constructTree(arr, float('-inf'), float('inf'))
            
            



        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans