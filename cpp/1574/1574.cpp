#include <vector>
#include <algorithm>
#include <iostream>

class Solution {
public:
    int findLengthOfShortestSubarray(std::vector<int>& arr) {
        std::vector<int> result;


        for (int i = 0; i < arr.size(); ++i)
        {
            bool willEnsureIncrease = true; 
            for (int j = i + 1; j < arr.size(); ++j)
            {
                if (arr.at(i) > arr.at(j))
                {
                    willEnsureIncrease = false;
                    break;
                }

                if (willEnsureIncrease && (result.size() == 0 || result.at(result.size() - 1)))
                {
                    result.emplace_back(arr.at(i));
                }
            }
        }
        
        for (const auto elm : arr)
        {
            if (result.size() == 0 || result.at(result.size() - 1) < elm)
            {
                result.emplace_back(elm);
            }
        }
        return arr.size() - result.size();
    }
};

int main()
{
    Solution s;
    std::vector<int> vec = {1, 2, 3, 10, 4, 2, 3, 5};
    std::cout << s.findLengthOfShortestSubarray(vec) << "\n";
}
