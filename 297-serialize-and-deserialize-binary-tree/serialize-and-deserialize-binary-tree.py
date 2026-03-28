# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        q = deque([root])
        res = ''
        while (q):
            curr = q.popleft()
            if not curr:
                res += 'None,'
                continue
            res += str(curr.val) +','
            q.append(curr.left)
            q.append(curr.right)
        print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        lst = data.split(',')
        root = TreeNode(lst[0])
        q = deque([root])
        i = 1
        while (q and i < len(lst)):
            curr = q.popleft()
            if lst[i] != 'None':
                left = TreeNode(int(lst[i]))
                curr.left = left
                q.append(left)
            i += 1
            if lst[i] != 'None':
                right = TreeNode(int(lst[i]))
                curr.right = right
                q.append(right)
            i += 1
        return root

            

        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))