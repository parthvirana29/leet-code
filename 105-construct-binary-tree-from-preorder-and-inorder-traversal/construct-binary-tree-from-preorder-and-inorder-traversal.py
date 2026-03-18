# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

      # preorder = 3, 9, 10, 11, 12, 20, 15, 7
        # inorder = 12, 10, 9, 11, 3, 15, 20, 7
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # [3,9,20,15,7]
        # [9,*3*,15,20,7]
        if (not preorder):
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        


