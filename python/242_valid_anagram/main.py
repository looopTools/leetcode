import unittest

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for elm in t:
            s = s.replace(elm, '', 1)
        return len(s) == 0

    def isAnagramTwo(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        for i in range(0, len(s)):
            if s[i] != t[i]:
                return False
        return True

    def isAnagramThree(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        s_data = {}
        t_data = {}

        for i in range(0, len(s)):

            if not s[i] in s_data:
                s_data[s[i]] = 0
            if not t[i] in t_data:
                t_data[t[i]] = 0
            s_data[s[i]] = s_data[s[i]] + 1
            t_data[t[i]] = t_data[t[i]] + 1                

        for key in s_data:
            if key not in t_data or s_data[key] != t_data[key]:
                return False

        return True

        
    
class TestSolution(unittest.TestCase):

    def test_is_anagram(self):

        solution = Solution()
        self.assertTrue(solution.isAnagram('anagram', 'nagaram'))
        self.assertFalse(solution.isAnagram('rat', 'car'))
        self.assertFalse(solution.isAnagram('a', 'ab'))
        self.assertFalse(solution.isAnagram('ac', 'bb'))
        

    def test_is_anagram_two(self):

        solution = Solution()
        self.assertTrue(solution.isAnagramTwo('anagram', 'nagaram'))
        self.assertFalse(solution.isAnagramTwo('rat', 'car'))
        self.assertFalse(solution.isAnagramTwo('a', 'ab'))
        self.assertFalse(solution.isAnagramTwo('ac', 'bb'))        

    def test_is_anagram_three(self):

        solution = Solution()
        self.assertTrue(solution.isAnagramThree('anagram', 'nagaram'))
        self.assertFalse(solution.isAnagramThree('rat', 'car'))
        self.assertFalse(solution.isAnagramTwo('a', 'ab'))
        self.assertFalse(solution.isAnagramThree('ac', 'bb'))        
                
        
if __name__ == '__main__':
    unittest.main()
