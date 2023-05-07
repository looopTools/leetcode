#include <vector>

class Solution {
public:
    std::vector<int> searchRange(std::vector<int>& nums, int target) {
        int first = -1; 
        int last = -1;

        int index = 0;
        for (const auto& num : nums)
        {
            if (num == target)
            {
                if (first == -1)
                {
                    first = index;
                }
                last = index;
            }
            index = index + 1;
        }      

        return std::vector<int> {first, last};
    }
};
