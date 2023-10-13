class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        observed = {}

        for index in range(0, len(nums)):

            if not nums[index] in observed:
                observed[nums[index]] = [index]
            elif nums[index] in observed:
                for elm in observed[nums[index]]:
                    if abs(elm  - index) <= k:
                        return True
                observed[nums[index]].append(index)
        return False


    
def evaluate(nums: list[int], k: int, expected_value: bool, solution: Solution):

    result = expected_value == solution.containsNearbyDuplicate(nums, k)
    print(f"Success: {result} for List {nums} with k value: {k}, expected value: {expected_value}")

if __name__ == "__main__":

    solution = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    expected_value = True

    evaluate(nums, k, expected_value, solution)


    solution = Solution()
    nums = [1, 0, 1, 1]
    k = 1
    expected_value = True

    evaluate(nums, k, expected_value, solution)

    solution = Solution()
    nums = [1,2,3,1,2,3]
    k = 2
    expected_value = False

    evaluate(nums, k, expected_value, solution)
            
