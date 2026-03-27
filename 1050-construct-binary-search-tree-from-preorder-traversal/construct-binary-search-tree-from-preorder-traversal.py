# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructTree(self, preorder, lower_limit, upper_limit):
        
        if (self.idx == len(preorder)):
            return None
        node = TreeNode(preorder[self.idx])
        if  node.val > upper_limit or node.val < lower_limit:
            return None
        self.idx += 1
        node.left = self.constructTree(preorder, lower_limit, node.val)
        node.right = self.constructTree(preorder, node.val, upper_limit)
        return node

    # using global idx (self.idx) b/c if we pass it as parameters the second call for node.right to construct right subtree won't get the correct idx. It'll still refer to idx value from the current call stack
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0
        return self.constructTree(preorder, float('-inf'), float('inf'))

        
        