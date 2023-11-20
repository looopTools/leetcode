import unittest

class Solution(object):
    def addStrings(self, num1: str, num2: str) -> str:
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1, num2 = self.get_smallest_then_biggest(num1, num2)

        index_num1 = len(num1) -1
        index_num2 = len(num2) -1
        remainder = 0

        while index_num1 > -1:
            res = remainder + int(num1[index_num1]) + int(num2[index_num2])
            if res >= 10:
                remainder = 1
                res = res - 10
            else:
                remainder = 0
            num2[index_num2] = str(res)
            index_num1 = index_num1 - 1
            index_num2 = index_num2 - 1
        
        if remainder != 0 and index_num2 != -1:
            while index_num2 != -1:
                res = remainder + int(num2[index_num2])
                if res >= 10:
                    remainder = 1
                    res = res - 10
                else:
                    remainder = 0
                num2[index_num2] = str(res)
                index_num2 = index_num2 - 1
        if remainder != 0:
            num2.insert(0, str(remainder))
        return ''.join(num2)

            
    def get_smallest_then_biggest(self, num1: str, num2: str) -> (list[str],list[str]):

        if len(num1) <= len(num2):
            return list(num1), list(num2)
        else:
            return list(num2), list(num1)

class TestSolution(unittest.TestCase):

    def test_add_strings(self):
        solution = Solution()
        self.assertEqual(solution.addStrings("11", "123"), "134")
        self.assertEqual(solution.addStrings("456", "77"), "533")
        self.assertEqual(solution.addStrings("0", "0"), "0")
        self.assertEqual(solution.addStrings("123456789", "987654321"), "1111111110")


if __name__ == '__main__':

    unittest.main()
