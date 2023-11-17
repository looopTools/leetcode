class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0: 
            return False 
        if n == 1: 
            return True
        
        i = 3

        while i < n:
            i = i * 3

        return i == n
