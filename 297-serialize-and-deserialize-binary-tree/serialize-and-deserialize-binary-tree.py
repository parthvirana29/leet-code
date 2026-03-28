class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        
        def preorder(node, string):
            if not node:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = preorder(node.left, string)
                string = preorder(node.right, string)
                # 1,2,None, None, 3, 4, None, None, 5, None, None
            return string
        print(preorder(root,''))
        return preorder(root,'')
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def undo_preorder(lst):
            if lst[0] == 'None':
                lst.pop(0)
                return None
            root = TreeNode(lst[0])
            lst.pop(0)
            root.left = undo_preorder(lst)
            root.right = undo_preorder(lst)
            return root

        
        data_list = data.split(',')
        root = undo_preorder(data_list)
        return root