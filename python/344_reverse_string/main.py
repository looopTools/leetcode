import unittest

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        i = 0
        j = len(s) - 1

        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i = i + 1
            j = j - 1 

class SolutionTakeTwo:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        i = 0
        j = len(s) - 1

        while i < j:
            s[i] = chr(ord(s[i]) ^ ord(s[j]))
            s[j] = chr(ord(s[i]) ^ ord(s[j]))
            s[i] = chr(ord(s[i]) ^ ord(s[j]))
            i = i + 1
            j = j - 1 
            
class TestSolution(unittest.TestCase):

    def test_reverse_string(self):
        s = Solution()

        data = ['h', 'e', 'l', 'l', 'o']
        exp = ['o', 'l', 'l', 'e', 'h']
        s.reverseString(data)
        self.assertEqual(data, exp)

        data = ['H', 'a', 'n', 'n', 'a', 'h']
        exp = ['h', 'a', 'n', 'n', 'a', 'H']
        s.reverseString(data)
        self.assertEqual(data, exp)

    def test_reverse_string(self):
        s = SolutionTakeTwo()

        data = ['h', 'e', 'l', 'l', 'o']
        exp = ['o', 'l', 'l', 'e', 'h']
        s.reverseString(data)
        self.assertEqual(data, exp)

        data = ['H', 'a', 'n', 'n', 'a', 'h']
        exp = ['h', 'a', 'n', 'n', 'a', 'H']
        s.reverseString(data)
        self.assertEqual(data, exp)        
if __name__ == '__main__':

    unittest.main()
