# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def inorder(self, root, arr):
        if (not root):
            return
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
        return arr
    
    def preorder(self, root, arr):
        if (not root):
            return
        arr.append(root.val)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)
        return arr

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

        res = self.inorder(root, [])
        print(res)
        res2 = self.preorder(root, [])
        print(res2)
        return str(res) + 'X' + str(res2)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        if not data or data == "[]X[]":
            return None
    
        # Split the data back into inorder and preorder
        parts = data.split('X')
        inorder = eval(parts[0])   # Convert string representation back to list
        preorder = eval(parts[1])
        
        if not inorder or not preorder:
            return None
        
        # Build a hashmap for quick index lookup in inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Helper function to build tree
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            # First element in preorder is always the root
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find root position in inorder
            root_idx = inorder_map[root_val]
            
            # Number of nodes in left subtree
            left_size = root_idx - in_start
            
            # Recursively build left and right subtrees
            root.left = build(
                pre_start + 1,           # Left subtree starts after root in preorder
                pre_start + left_size,   # Left subtree ends after left_size elements
                in_start,                # Left subtree starts at beginning in inorder
                root_idx - 1             # Left subtree ends before root in inorder
            )
            
            root.right = build(
                pre_start + left_size + 1,  # Right subtree starts after left subtree
                pre_end,                     # Right subtree goes to end
                root_idx + 1,                # Right subtree starts after root in inorder
                in_end                       # Right subtree goes to end
            )
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans