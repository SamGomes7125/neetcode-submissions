# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        import math
        
        def maxDepth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            
            depth = 1 + max(left_depth, right_depth)
            return depth

        if root is None:
            return True
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        if abs(left_depth - right_depth) > 1:
            return False
        return(
        self.isBalanced(root.left) and
        self.isBalanced(root.right)
        )
        
        