class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = list()
        return self.travers(root, values)

    def travers(self, node: TreeNode, values: List[int]) -> List[int]:

        if node is None:
            return values


        if node.left is not None: 
            values = self.travers(node.left, values)


        if node.right is not None: 
            values = self.travers(node.right, values)
        
        values.append(node.val)            
        return values

        
