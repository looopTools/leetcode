import unittest
from dataclasses import dataclass

@dataclass
class Entry:
    index: int
    count: int
    
class Solution:

    def firstUniqChar(self, s: str) -> int:
        map = {}

        for i in range(0, len(s)):
            if s[i] not in map:
                
                map[s[i]] = Entry(i, 1)
            else:
                map[s[i]].count += 1

        for key, entry in map.items():
            if entry.count == 1:
                return entry.index
        return -1
        
class TestSolution(unittest.TestCase):

    def test_solution(self):

        s = Solution()
        self.assertTrue(s.firstUniqChar("leetcode") == 0)
        self.assertTrue(s.firstUniqChar("loveleetcode") == 2)
        self.assertTrue(s.firstUniqChar("abba") == -1)

if __name__ == '__main__':
    unittest.main()
