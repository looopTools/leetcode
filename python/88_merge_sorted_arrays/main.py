import unittest

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if len(nums1) < m + n or n == 0:
            return 
        
        if m == 0:
            for i in range(0, len(nums2)):
                nums1[i] = nums2[i]
            return

        i = 0
        j = 0

        while j != n and i != m:

            if nums1[i] <= nums2[j]:
                i = i + 1
            if nums1[i] > nums2[j]:
                k = m
                while k >= i:
                    nums1[k] = nums1[k-1]
                    k = k - 1
            
                nums1[i] = nums2[j]
                m = m + 1
                j = j + 1
                i = i + 1

        if j < n:                  
            while j < n:           
                nums1[i] = nums2[j]
                m = m + 1          
                i = i + 1          
                j = j + 1          
        

            
            

class TesSolution(unittest.TestCase):

    def test_merge(self):

        solution = Solution()

        nums_1 = [1,2,3,0,0,0]
        nums_2 = [2,5,6]
        solution.merge(nums_1, 3, nums_2, 3)
        self.assertEqual(nums_1, [1,2,2,3,5,6])

        nums_1 = [1]
        nums_2 = []
        solution.merge(nums_1, 1, nums_2, 0)
        self.assertEqual(nums_1, [1])        
        
        nums_1 = [0]
        nums_2 = [1]
        solution.merge(nums_1, 0, nums_2, 1)
        self.assertEqual(nums_1, [1])

        nums_1 = [2, 0]
        nums_2 = [1]
        solution.merge(nums_1, 1, nums_2, 1)
        self.assertEqual(nums_1, [1, 2])
        


if __name__ == '__main__':
    unittest.main()
