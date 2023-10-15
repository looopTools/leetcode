# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        return self.travers(root, val)
        

    def travers(self, node, val):

        if not node:
            return None

        if node.val == val:
            return node

        if val < node.val:
            return self.travers(node.left, val)
        else:
            return self.travers(node.right, val)
        
    
