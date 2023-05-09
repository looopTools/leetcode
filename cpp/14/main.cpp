#include <cstddef>
#include <string>
#include <vector>
#include <sstream>

#include <iostream>

class Solution {
    
public:
    std::string longestCommonPrefix(std::vector<std::string>& strs)
    {
        size_t shortest_str_index = index_of_shortest(strs);
        std::string shortests = strs.at(shortest_str_index);

        std::stringstream ss;

        for (size_t char_index = 0; char_index < shortests.size(); ++char_index)
        {
            bool not_found = false;
            for (size_t str_index = 0; str_index < strs.size(); ++str_index)
            {
                if (strs.at(str_index).at(char_index) != shortests.at(char_index))
                {
                    not_found = true;
                    break;
                }
            }

            if (not_found)
            {
                break;
            }

            ss << shortests.at(char_index);
            
        }

        return ss.str();
        
        
    }

    std::size_t index_of_shortest(const std::vector<std::string>& strs)
    {
        size_t index = 0;
        size_t size = strs.at(0).length();
        for (size_t i = 1; i < strs.size(); ++i)
        {
            if (size > strs.at(i).length())
            {
                index = i;
                size = strs.at(0).length();
            }
        }
        return index;
    }
};

int main(void)
{
    
    Solution s;

    std::vector<std::string> data = {"flower", "flow", "flight"};
    std::cout << s.longestCommonPrefix(data) << "\n";
    data = {"dog", "racecar", "car"};
    
    std::cout << s.longestCommonPrefix(data) << "\n";    
    
}
