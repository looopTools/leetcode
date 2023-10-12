# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.travers(root, False)
        
    def travers(self, node, is_left):
        if not node:
            return 0

        if is_left and not node.right and not node.left:
            return node.val
        
        return self.travers(node.left, True) + self.travers(node.right, False)
