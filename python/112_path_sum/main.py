# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def travers(self, node, value, targetSum):

        value = value + node.val

        if not node.left and not node.right: 
            return value == targetSum
                
        result = False
        
        if node.left:
            result = self.travers(node.left, value, targetSum)
            
        # Short circut travets
        if result:
            return result

        if node.right:
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


        



        
