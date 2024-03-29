class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.travers(root, 0)
        
    def travers(self, node, length):
        if not node: 
            return length 
        length = length + 1
        left_length = self.travers(node.left, length)
        right_length = self.travers(node.right, length)

        if left_length > right_length: 
            return left_length
        else: 
            return right_length
        
