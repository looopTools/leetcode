#include <iostream>

#include <string>

#include <algorithm>

class Solution {
public:
    int myAtoi(std::string s) {
        int result = 0; 

        int multiplier = 1; 

        bool is_negative = false;

        bool number_read = false;

        for (auto it = s.end() - 1; it >= s.begin(); --it)
        {
            if (_zero_ascii <= int(*it) && int(*it) <= _nine_ascii)
            {
                number_read = true;
                result = std::clamp(result + ((static_cast<int>(*it) - _zero_ascii) * multiplier), INT_MIN, INT_MAX);
                multiplier = multiplier * 10;
            }
            else if ((*it) == _minus_ascii)
            {
                is_negative = true;
            }
            else if ((*it) == _plus_ascii)
            {
                is_negative = false;
            }
            else if ((*it) != _whitespace_ascii && number_read)
            {
                return 0;
            }
            // Todo what is clamping 
        }

        return is_negative ? (-1 * result) : result;
    }
private:    
    static constexpr int _zero_ascii = 48;
    static constexpr int _nine_ascii = 57;
    static constexpr int _minus_ascii = 45;
    static constexpr int _plus_ascii = 43;
    static constexpr int _whitespace_ascii = 32;
};


int main(void)
{
    Solution s;
    std::cout << std::to_string(s.myAtoi("42")) << "\n";
    std::cout << std::to_string(s.myAtoi("-91283472332")) << "\n";
}
