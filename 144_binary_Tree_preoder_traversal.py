# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = list()
        return self.travers(root, values)
    def travers(self, node: TreeNode, values: List[int]) -> List[int]:

        if node is None:
            return values

        values.append(node.val)

        if node.left is not None: 
            values = self.travers(node.left, values)
        
        if node.right is not None: 
            values = self.travers(node.right, values)

        return values

        
