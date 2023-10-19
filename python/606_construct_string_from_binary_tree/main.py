from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""
        if root:
            result = self.travers(root)
        return result
    
    def travers(self, node: TreeNode) -> str:
        if not node:
            return None 
        left = self.travers( node.left)
        right = self.travers(node.right)

        result = None
        if left and right:
            result = f"{node.val}({left})({right})"
        elif left and not right:
            result = f"{node.val}({left})"            
        elif not left and right:
            result = f"{node.val}()({right})"
        else:
             result = f"{node.val}"
        
        return result


def test(tree: TreeNode, expected: str, solution: Solution):

    result = solution.tree2str(tree) == expected

    print(f"Result: {result} for expected: {expected}")

if __name__ == "__main__":

    solution = Solution()

    tree = TreeNode(val=1,left=TreeNode(val=2, left=TreeNode(val=4)),  right=TreeNode(val=3))
    expected = "1(2(4))(3)"

    test(tree, expected, solution)

    tree = TreeNode(val=1,left=TreeNode(val=2, right=TreeNode(val=4)),  right=TreeNode(val=3))
    expected = "1(2()(4))(3)"

    test(tree, expected, solution)
        
