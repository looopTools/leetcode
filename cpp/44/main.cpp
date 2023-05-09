#include <string>

#include <iostream>

class Solution {
public:
    bool isMatch(std::string s, std::string p) {

        auto s_it = s.begin();
        auto p_it = p.begin();

        while(p_it != p.end() && s_it != s.end())
        {
            if (*s_it == *p_it || *p_it == accept_any)
            {
                s_it = s_it + 1;
                p_it = p_it + 1; 
            }
            else if (*p_it == accept_all)
            {
                if (*s_it == *(p_it + 1))
                {
                    p_it = p_it + 2;
                }
                s_it = s_it + 1;
            }
            else
            {
                return false; 
            }
        }

        while(*p_it == accept_all)
        {
            p_it = p_it + 1;
        }
        return s_it == s.end() && (p_it == p.end() || p_it == p.end() - 1);
    }

    

private:
    char accept_any = '?';
    char accept_all = '*';
        
};


std::string bool_to_str(const bool val)
{
    return val ? "True" : "False";
}

void assert_result(const bool expected, const bool val)
{
    std::cout << "Expected: " << bool_to_str(expected) << " acctual: " << bool_to_str(val) << "\n";
}



int main(void)
{

    Solution s;
    assert_result(s.isMatch("aa", "a"), false);
    assert_result(s.isMatch("aa", "*"), true);
    assert_result(s.isMatch("cb", "?a"), false);
    assert_result(s.isMatch("adceb", "*a*b"), true);
    assert_result(s.isMatch("acdcb", "a*c?b"), false);
    assert_result(s.isMatch("a", "aa"), false);
    assert_result(s.isMatch("a", "a*"), true);
    assert_result(s.isMatch("a", "*"), true);
    assert_result(s.isMatch("", "*"), true);
    assert_result(s.isMatch("", "**"), true);
    assert_result(s.isMatch("", "*******"), true);    
    

}
