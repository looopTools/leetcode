class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()
        s = "".join([c for c in s if self.isAlphaNumerical(c)])
        
        if len(s) == 0:
            return True 


        i = 0
        j = len(s) - 1

        while i < j:
            print(i)
            if not s[i] == s[j]:
                return False
            i = i + 1
            j = j - 1
            
        return True

    def isAlphaNumerical(self, character):

        decValue = ord(character)

        return (48 <= decValue and decValue <= 57) or (97 <= decValue  and decValue <= 122)

if __name__ == "__main__":

    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
    print(solution.isPalindrome("race a car"))
    print(solution.isPalindrome(" "))
    print(solution.isPalindrome("aa"))    

    s = "A man, a plan, a canal: Panama"
    s = "".join([c for c in s if solution.isAlphaNumerical(c)])
    print(s)
    
    
