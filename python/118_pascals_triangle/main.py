import unittest

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result = list()

        for row in range(0, numRows):
            row_entry = list()
            for col in range(0, row + 1):
                if col == 0 or col == row:
                    row_entry.append(1)
                else:
                    val = result[row-1][col-1] + result[row-1][col]
                    row_entry.append(val)
            result.append(row_entry)
        return result 

class TestMyGenerater(unittest.TestCase):

    def test_genearter(self):
        solution = Solution()
        self.assertEqual([[1]], solution.generate(1))        
        self.assertEqual([[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], solution.generate(5))


if __name__ == "__main__":
    unittest.main()
