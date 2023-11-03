import unittest

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 4 or n == 1:
            return True 
        pow = 4

        while pow < n:
            pow = pow * 4
        
        return pow == n

class TestSolution(unittest.TestCase):

    def test_isPowerOfFour(self):
        solution = Solution()
        self.assertTrue(solution.isPowerOfFour(16))
        self.assertFalse(solution.isPowerOfFour(8))
        self.assertTrue(solution.isPowerOfFour(1))        

if __name__ == "__main__":
    unittest.main()
