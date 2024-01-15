import unittest

class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        first = ord(word[0]) >= 65 and ord(word[0]) <= 90
        number_of_caps = 0 
        for i in range(0, len(word)):
            if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                number_of_caps = number_of_caps + 1
        return number_of_caps == 0 or (number_of_caps == 1 and first) or number_of_caps == len(word)
            

    def __is_capital(self, val: int) -> bool:

        return val >= 65 and val <= 90




class TestSolution(unittest.TestCase):

    def test_solution(self):

        solution = Solution()
        self.assertTrue(solution.detectCapitalUse('jon'))
        self.assertTrue(solution.detectCapitalUse('USA'))
        self.assertTrue(solution.detectCapitalUse('Flag'))
        self.assertFalse(solution.detectCapitalUse('FLaG'))

if __name__ == '__main__':

    unittest.main()
