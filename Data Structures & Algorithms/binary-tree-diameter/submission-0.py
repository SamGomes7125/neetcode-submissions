# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        def maxDepth(root: Optional[TreeNode]) -> int:

            if root is None:
                return 0

            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)

            depth = 1 + max(left_depth, right_depth)

            return depth

        leftHeight = maxDepth(root.left)
        rightHeight = maxDepth(root.right)

        d = leftHeight + rightHeight

        dl = self.diameterOfBinaryTree(root.left)
        dr = self.diameterOfBinaryTree(root.right)

        if dl > d:
            d = dl

        if dr > d:
            d = dr

        return d