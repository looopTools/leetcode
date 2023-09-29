class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if not p and not q:
            return True 
            
        if (p and not q) or (not p and q) or (p.val != q.val):
            return False

        if not self.isSameTree(p.left, q.left):
            return False
        
        if not self.isSameTree(p.right, q.right):
            return False

        return True
        
