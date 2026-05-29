# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        def isSameTree(p,q) -> bool:
            if p is None and q is None:
                return True
            if p is None and q is not None:
                return False
            if q is None and p is not None:
                return False
            if p.val != q.val:
                return False
            left_tree = isSameTree(p.left,q.left)
            right_tree = isSameTree(p.right,q.right)
            return left_tree and right_tree
        if root.val == subRoot.val:
            if isSameTree(root,subRoot):
                return True
            else:
                    return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        else:
                return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        