class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
class Solution:
    def maxDepth(self, root: Node) -> int:
        if root is not None:
            return self.travers(root)
        return 0

    def travers(self, node: Node) -> int:

        if len(node.children) == 0:
            return 1

        longest = 0 
        for child in node.children:
            length = self.travers(child)
            if length > longest:
                longest = length
        return longest + 1
    
