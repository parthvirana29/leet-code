# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        q = deque([(root, 0)])
        while q:
            node, pathSum = q.popleft()
            newPathSum = pathSum + node.val
            if not node.left and not node.right:
                if newPathSum == targetSum:
                    return True
            else:
                if node.left:
                    q.append((node.left, newPathSum))

                if node.right:
                    q.append((node.right, newPathSum))

        return False