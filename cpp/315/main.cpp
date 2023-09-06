#include <vector>
#include <map>

#include <cstdlib>

#include <iostream>
#include <string>

class Solution {
public:

    void print(const std::map<int, int>& appearence)
    {
        std::cout << "{\n";
        for (const auto& [key, value] : appearence)
        {
            std::cout << "\t{" << std::to_string(key) << ":" << std::to_string(value) << "}\n";
        }
        std::cout << "}\n";
    }

    int less_than(const int val, const std::map<int, int>& appearence)
    {
        int less = 0;
        for (const auto& [key, value] : appearence)
        {
            if (key >= val)
            {
                break;
            }
            if (key < val)
            {
                less = less + value;
            }
        }
        return less;
    }
    std::vector<int> countSmaller(std::vector<int>& nums) {
        
        if (nums.empty())
        {
            return nums;
        }

        std::map<int, int> appearence; 

        for (int i = nums.size() -1; i >= 0; --i)
        {
            int less =  less_than(nums[i],  appearence);
            if (appearence.find(nums[i]) == appearence.end())
            {
                appearence[nums[i]] = 1;
            }
            else
            {
                appearence[nums[i]] = appearence[nums[i]] + 1;
            }
            nums[i] = less;
        }
        print(appearence);
        return nums;    
    }
};


int main(void)
{
    std::vector<int> vec = {5, 2, 6, 1};
    Solution s;
    for (const auto& elm :s.countSmaller(vec))
    {
        std::cout << std::to_string(elm) << " ";
    }

    std::cout << "\n";
}
