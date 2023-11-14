import unittest

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        result = None
        i = 0

        
        found = list()
        while i < len(nums):
            if nums[i] in found:

                for j in range(0, len(nums)):
                    if j + 1 not in nums:
                        return [nums[i], j + 1]
            found.append(nums[i])
            i = i + 1
        return result

class TestSolution(unittest.TestCase):

    def test_find_error_nums(self):
        solution = Solution()
        self.assertEqual(solution.findErrorNums([1, 2, 2, 4]), [2, 3])
        self.assertEqual(solution.findErrorNums([1, 1]), [1, 2])
        self.assertEqual(solution.findErrorNums([2, 2]), [2, 1])
        self.assertEqual(solution.findErrorNums([3,2,2]), [2, 1])
        self.assertEqual(solution.findErrorNums([3,2,3,4,6,5]), [3, 1])
        self.assertEqual(solution.findErrorNums([3,3,1]), [3, 2])                                

if __name__ == '__main__':

    unittest.main()
