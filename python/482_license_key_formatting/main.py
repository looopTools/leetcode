import unittest

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        without_dashes = s.replace('-', '')
        len_first_group = len(without_dashes) % k

        i = 0
        res = ''
        if len_first_group != 0:
            res = f'{without_dashes[0:len_first_group]}'
            i = len_first_group

        while i < len(without_dashes):
            if i != 0:
                res = f'{res}-{without_dashes[i:i + k]}'
            else:
                res = f'{res}{without_dashes[i:i + k]}'
            i = i + k
            
        return res.upper()

class TestSolution(unittest.TestCase):

    def test_licenseKeyFormatting(self):
        solution = Solution()
        self.assertEqual(solution.licenseKeyFormatting('5F3Z-2e-9-w', 4), '5F3Z-2E9W')
        self.assertEqual(solution.licenseKeyFormatting('2-5g-3-J', 2), '2-5G-3J')        


if __name__ == '__main__':

    unittest.main()
