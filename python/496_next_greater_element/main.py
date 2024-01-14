import unittest

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        result = list()

        for i in range(0, len(nums1)):
            res = -1
            for j in range(i, len(nums2)):
                if nums1[i] < nums2[j]:
                    res = nums2[j]
                    break
            result.append(res)
        return result
        
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        solution = Solution()
        self.assertTrue([-1, 3, -1], solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
        self.assertTrue([3, -1], solution.nextGreaterElement([2, 4], [1, 2, 3, 4]))
        

if __name__ == '__main__':

    unittest.main()
