import unittest

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result = list()

        for row in range(0, rowIndex + 1):
            row_entry = list()
            for col in range(0, row + 1):
                if col == 0 or col == row:
                    row_entry.append(1)
                else:
                    val = result[col-1] + result[col]
                    row_entry.append(val)

            result = row_entry 
        return result 

class TestMyGenerater(unittest.TestCase):

    def test_genearter(self):
        solution = Solution()
        self.assertEqual(solution.getRow(3), [1,3,3,1])
        self.assertEqual(solution.getRow(0), [1])
        self.assertEqual(solution.getRow(1), [1, 1])                        


if __name__ == "__main__":
    unittest.main()
