#include <string>
#include <map>

#include <iostream>

class Solution {
public:
    int romanToInt(std::string s) {

        int result = 0;

        size_t index = 0;
        size_t increment = 0;        
        while (index < s.size() - 1)
        {

            if (_numerials.at(s.at(index)) < _numerials.at(s.at(index + 1)))
            {
                result = result + _numerials.at(s.at(index + 1)) - _numerials.at(s.at(index));
                increment = 2;
            }
            else
            {
                result = result + _numerials.at(s.at(index));
                increment = 1;
            }
            index = index + increment;
        }

        if (index < s.size())
        {
            result = result + _numerials.at(s.at(index));
        }
        
        return result;
        
    }

private:
    std::map<char, int> _numerials
    {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };
};


int main(void)
{
    Solution s;
    std::cout << "Roman III: " << std::to_string(s.romanToInt("III")) << "\n";
    std::cout << "Roman LVIII: " << std::to_string(s.romanToInt("LVIII")) << "\n";
    std::cout << "Roman MCMXCIV: " << std::to_string(s.romanToInt("MCMXCIV")) << "\n";
}
