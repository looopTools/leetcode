import unittest

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        
        nums = list(set(nums))
        nums.sort(reverse=True)
        
        if len(nums) < 3:
            return nums[0]
        else:
            return nums[2]
        


class TestSolution(unittest.TestCase):

    def test_third_max(self):
        solution = Solution()

        self.assertEqual(solution.thirdMax([3, 2, 1]), 1)
        self.assertEqual(solution.thirdMax([1, 2]), 2)
        self.assertEqual(solution.thirdMax([2, 2, 3, 1]), 1)

if __name__ == '__main__':

    unittest.main()
