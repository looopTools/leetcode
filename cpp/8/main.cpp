#include <string>
#include <iostream>

class Solution {
public:
    int myAtoi(std::string s) {
     
        const int diff = 48; 
        int num = 0;
        int offset = 1;
        bool positive = true;
        for(size_t i = s.size(); i > 0; --i)
        {
            char chr = s[i - 1];
            if (chr == '-' || chr == '+')
            {
                if (chr == '-')
                {
                    positive = false;
                    break;
                }
            }
            if (48 <= (int)chr &&  (int)chr <= 57)
            {
                num = num + (offset * (((int)chr) - diff));
                offset = offset * 10;
            }
            else
            {
                break;
            }
            
        }       
        return positive ? num : (-1 * num);
    }
};

int main()
{

    Solution s;

    std::string str = "42";
    std::cout << std::to_string(s.myAtoi(str)) << "\n";

    str = "-142";
    std::cout << std::to_string(s.myAtoi(str)) << "\n";

    str = "4193 with words";
    std::cout << std::to_string(s.myAtoi(str)) << "\n";    
    
}
