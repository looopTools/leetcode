class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        j = 0

        for i in range(0, len(s)):

            found = False
            while j < len(t):
                if s[i] == t[j]:
                    found = True
                    j = j + 1
                    break
                j = j + 1

            if not found:
                return False
            i = i + 1
            
        return True
                            
def test(s: str, t: str, expected_value: bool, solution: Solution):

    result = solution.isSubsequence(s, t) == expected_value

    print(f"Result: {result} for s: {s} and t: {t} expected value: {expected_value}")

if __name__ == "__main__":

    solution = Solution()
    test("abc", "ahbgdc", True, solution)
    test("axc", "ahbgdc", False, solution)
    test("acb", "ahbgdc", False, solution)
