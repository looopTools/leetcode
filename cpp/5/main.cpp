#include <string>

#include <iostream>

class Solution {
public:
    std::string longestPalindrome(std::string s) {

        if (s.size() <= 1)
        {
            return s;
        }
        
        std::string longest_palindrom = "";

        for (size_t i = 0; i < s.size() - 1; ++i)
        {            
            for (size_t j = s.size() - 1; j > i; --j)
            {
                std::string sub_string = s.substr(i, j);
                if (is_palindrom(sub_string) && longest_palindrom.size() < sub_string.size())
                {
                    longest_palindrom = sub_string;
                }
            }

            if (s.size() - i < longest_palindrom.size())
            {
                break;
            }
        }
        return longest_palindrom;
    }

private:

    bool is_palindrom(const std::string& str)
    {
        auto start_it = str.begin();
        auto end_it = str.end() - 1;

        while (start_it < end_it)
        {
            if (*start_it != *end_it)
            {
                return false; 
            }
            start_it++;
            end_it--;
        }

        return true;
    }
};


int main(void)
{
    Solution s;
    std::cout << s.longestPalindrome("babad") << "\n";
    std::cout << s.longestPalindrome("cbbd") << "\n";    
}
