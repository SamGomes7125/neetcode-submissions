# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def inorder(node):
            if node is None:
                return
            result = inorder(node.left)
            if result is not None:
                return result
            self.k -= 1
            if self.k == 0:
                return node.val
            else:
                result = inorder(node.right)
                if result is not None:
                    return result
        return inorder(root)
            

            