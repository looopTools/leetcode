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

    def thirdMaxTwo(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = None
        m = None
        s = None
        
        for num in nums:
            if l is None or num >= l:
                if num != l:
                    s = m
                    m = l
                l = num
            elif m is None or num >= m:
                if num != m:
                    s = m
                m = num
            elif s is None or num >= s:
                s = num
        if len (nums) < 3 or s is None:
            return l
        return s

    


class TestSolution(unittest.TestCase):

    def test_third_max(self):
        solution = Solution()

        self.assertEqual(solution.thirdMax([3, 2, 1]), 1)
        self.assertEqual(solution.thirdMax([1, 2]), 2)
        self.assertEqual(solution.thirdMax([2, 2, 3, 1]), 1)

    def test_third_maxTwo(self):
        solution = Solution()

        self.assertEqual(solution.thirdMaxTwo([3, 2, 1]), 1)
        self.assertEqual(solution.thirdMaxTwo([1, 2]), 2)
        self.assertEqual(solution.thirdMaxTwo([1, 1, 2]), 2)        
        self.assertEqual(solution.thirdMaxTwo([2, 2, 3, 1]), 1)
        self.assertEqual(solution.thirdMaxTwo([1,2,-2147483648]), -2147483648)

        

if __name__ == '__main__':

    unittest.main()
