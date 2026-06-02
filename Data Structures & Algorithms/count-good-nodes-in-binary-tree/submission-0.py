# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = []
        if root is None:
            return len(good_nodes)
        else:
            max_value = root.val
            good_nodes.append(root)
            def findGoodNodes(root,max_value):
                if root is None:
                    return
                if root.val >= max_value:
                    max_value = root.val
                    good_nodes.append(root)
                findGoodNodes(root.left,max_value)
                findGoodNodes(root.right,max_value)
            findGoodNodes(root.left,max_value)
            findGoodNodes(root.right,max_value)
            return len(good_nodes)

        



        