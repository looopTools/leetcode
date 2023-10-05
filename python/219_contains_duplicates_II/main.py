class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        observed = {}

        for index in range(0, len(nums)):

            if not nums[index] in observed:
                observed[nums[index]] = index
            elif nums[index] in observed and abs(observed[nums[index]] - index) <= k:
                return True
        return False


    
