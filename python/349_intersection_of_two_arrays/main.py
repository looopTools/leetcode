import unittest

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        
        result = list()

        for elm in nums1:
            if elm not in result and elm in nums2:
                result.append(elm)
        
        return result


class TestSolution(unittest.TestCase):

    def test_intersection(self):
        solution = Solution()
        res = solution.intersection([1, 2, 2, 1], [2, 2])
        self.assertTrue(res ==[2])
        
        res = solution.intersection([4, 9, 5], [9, 4, 9, 8, 4])
        self.assertTrue( res == [9, 4] or res == [4, 9])
        return None 


if __name__ == '__main__':

    unittest.main()

