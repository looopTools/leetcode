# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def travers(self, node, value, targetSum):

        if node == None: 
            return value == targetSum
        

        value = value + node.val

        result = self.travers(node.left, value, targetSum)
        
        # Short circut travels
        if result:
            return result
        
        result = self.travers(node.right, value, targetSum)

        return result

    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        if root == None:
            return False

        return self.travers(root, 0, targetSum)


        



        
