import unittest

class Solution(object):
    def mySqrt(self, x):

        if x == 0 or x == 1:
            return x
        
        half = int(x / 2)
        return self.find_sqrt(x, half)

    def find_sqrt(self, x, half):
        if half * half == x:
            return half
        elif half * half > x:
            return self.find_sqrt(x, int(half / 2))
        elif half * half < x and (half + 1) * (half + 1) > x:
            return half
        elif half * half < x and (half + 1) * (half + 1) <= x:
            return self.find_sqrt(x, int(half + 1))
        else:
            return half

        
class TestMySqrt(unittest.TestCase):

    def test_mysqrt(self):
        solution = Solution()
        self.assertTrue(2 == solution.mySqrt(4))
        self.assertTrue(2 == solution.mySqrt(8))
        self.assertTrue(1 == solution.mySqrt(2))
        self.assertTrue(2 == solution.mySqrt(6))                        

# def test(x, expected, solution):a

#     result_value = solution.mySqrt(x)
#     result = expected == result_value

#     print(f'Result {result} for x: {x} with expected_result: {expected} with result value {result_value}')


if __name__ == "__main__":
    unittest.main()
    # solution =   Solution()
    # test(4, 2, solution)
    # test(8, 2, solution)
