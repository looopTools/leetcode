class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) > len(haystack):
            return -1


        result = -1 
        i = 0
    
        while i < len(haystack):
            substr = haystack[i: i + len(needle)]
            if  substr == needle:
                result = i
                break
            else:
                i = self.getNextIndex(substr, needle[0], len(needle), i)
                

        return result
    
    def getNextIndex(self, word, first_chr_needle, needle_length, current_index):

        result = -1
        for i in range(0, len(word)):
            if word[i] == first_chr_needle and i != 0:
                result = i
                break
        if result == -1:
            return current_index + needle_length
        else:
            return current_index + result

        

def test(haystack, needle, expected_value, solution):

    result = expected_value == solution.strStr(haystack, needle)
    print(f"Result {result} for haystack: {haystack} with needle {needle}")
    
if __name__ == "__main__":

    solution = Solution()
    test("sadbutsad", "sad", 0, solution)
    test("leetcode", "leeto", -1, solution)
