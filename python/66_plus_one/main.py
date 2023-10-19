class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if not digits:
            return digits
        
        digits[len(digits) - 1] = digits[len(digits) - 1] + 1
        
        remainder = 0
        for i in range(len(digits)-1, -1, -1):
            value = digits[i] +  remainder

            if value == 10: 
                digits[i] = 0
                remainder = 1
            else:
                digits[i] = value
                remainder = 0
                break

        if remainder != 0:
            digits.insert(0, 1)
        return digits
        

def test(number, expected, solution):
    digits = solution.plusOne(number)
    result = expected == digits
    print(f"{result} for {number} with expected {expected} resulting digits {digits}")


if __name__ == "__main__":

    solution = Solution()
    test([1, 2, 3], [1, 2, 4], solution)
    test([4, 3, 2, 1], [4, 3, 2, 2], solution)
    test([9], [1, 0], solution)
    test([9, 9], [1, 0, 0], solution)
