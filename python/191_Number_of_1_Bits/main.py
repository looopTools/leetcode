import unittest

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        number_of_ones = 0
        while n:
            number_of_ones = number_of_ones + (1 & n)
            n = n >> 1
        return number_of_ones

class TestSolution(unittest.TestCase):

    def test_hamming_weight(self):

        solution = Solution()

        n = int(0b00000000000000000000000000001011)
        self.assertTrue(solution.hammingWeight(n), 3)

        n = int(0b00000000000000000000000010000000)
        self.assertTrue(solution.hammingWeight(n), 1)

        n = int(0b11111111111111111111111111111101)
        self.assertTrue(solution.hammingWeight(n), 31)

            
if __name__ == '__main__':

    unittest.main()
