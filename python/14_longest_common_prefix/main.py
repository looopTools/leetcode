class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        shortest, index = self.shortest_string(strs)
        
        prefix = ""

        if prefix == shortest:
            return prefix


        for i in range(0, len(shortest)):
            stop = False
            for elm in strs:
                if shortest != elm and shortest[i] != elm[i]:
                    stop = True
                    
            if stop:
                break
            prefix = prefix + shortest[i]
        return prefix

    def shortest_string(self, strs: list[str]) -> (str, int):

        shortest = None
        index = -1 

        for i in range(0, len(strs)):
            if shortest == None or len(shortest) > len(strs[i]):
                shortest = strs[i]
                index = i

        return shortest, i
                
    


def test(strs: list[str], expected: str, solution: Solution):
    shortest = solution.longestCommonPrefix(strs)
    result = expected == shortest
    print(f"Result: {result} for strs {strs} with expected: {expected} shortest: {shortest}")


if __name__ == "__main__":

    solution = Solution()
    
    test(["flower","flow","flight"], "fl", solution)
    test(["dog","racecar","car"], "", solution)
    test(["", "b"], "", solution)        

