class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        prev_was_char = False
        if s:
            for chr in s: 
                if prev_was_char and chr == ' ':
                    count = count + 1
                    prev_was_char = False
                elif not prev_was_char and not chr == ' ':
                    prev_was_char = True
        if prev_was_char:
            count = count + 1
        return count


def test(s: str, expected_value: int, solution: Solution):

    segments = solution.countSegments(s)
    result =  segments == expected_value
    print(f"Result {result} for string {s} with expected value {expected_value} and segments: {segments}")

if __name__ == "__main__":

    solution = Solution()
    test("Hello, my name is John", 5, solution)
    test("                ", 0, solution)
