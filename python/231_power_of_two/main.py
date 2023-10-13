class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if not self.isEven(n):
            return False

        for exp in range(int(n/2), 0, -1):
            if 2**exp == n:
                return True
        return False
        
    def isEven(self, n: int):

        return n % 2 == 0

def evaluate(n: int, expected_value: bool, solution: Solution):

    result = expected_value == solution.isPowerOfTwo(n)

    print(f"Result: {result} for n: {n} with expected value: {expected_value}")


if __name__ == "__main__":

    solution = Solution()
    n = 1
    expected_value = True

    evaluate(n, expected_value, solution)

    solution = solution
    n = 16
    expected_value = True

    evaluate(n, expected_value, solution)

    solution = solution
    n = 3
    expected_value = False

    evaluate(n, expected_value, solution)    

    solution = solution
    n = 4
    expected_value = True

    evaluate(n, expected_value, solution)    
    
