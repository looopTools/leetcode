import unittest

class Solution:
    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # For this case 'y' and 'Y' are not considered vowels
        
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1
        i_is_vowel = False
        j_is_vowel = False
        while i < j:
            i_is_vowel = s[i] in self.vowels
            j_is_vowel = s[j] in self.vowels
            if i_is_vowel and j_is_vowel:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i = i + 1
                j = j - 1
            elif not i_is_vowel:
                i = i + 1
            elif not j_is_vowel:
                j = j - 1

        return ''.join(s)

class TestSolution(unittest.TestCase):

    def test_reverse_vowels(self):
        solution = Solution()

        self.assertEqual(solution.reverseVowels('hello'), 'holle')
        self.assertEqual(solution.reverseVowels('leetcode'), 'leotcede')        
        self.assertEqual(solution.reverseVowels('Yo! Bottoms up, U.S. Motto, boy!'), 'Yo! Bottoms Up, u.S. Motto, boy!')
if __name__ == '__main__':
    unittest.main()
