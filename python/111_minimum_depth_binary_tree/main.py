# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root: 
            return 0

        return self.travers(root, 0)
        

    def travers(self, node, length):
        if not node: 
            return length 

        length = length + 1

        left_length = None
        right_length = None

        if node.left:
            left_length = self.travers(node.left, length)
        if node.right:
            right_length = self.travers(node.right, length)

        if (left_length and left_length < right_length) or (left_length and not right_length): 
            return left_length 
        elif right_length:
            return right_length
        else:
            return length

        
