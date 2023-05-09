class Solution {
public:
    std::string longestCommonPrefix(std::vector<std::string>& strs) {

    // std::stringstream prefix;
std:string  prefix; 
    for (const auto c : strs.at(0))
    {
        prefix = prefix + c;
        if (!hasPrefix(prefix, strs))
        {
            prefix = prefix.substr(0, prefix.length() - 1);
            break; 
        }
        
    }

    return prefix; 
   
}

    bool starts_with(const std::string& str, const std::string& prefix)
{
    if (prefix.length() > str.length())
    {
        return false;
    }

    for (size_t i = 0; i < prefix.length(); ++i)
    {
        if (prefix.at(i) != str.at(i))
        {
            return false; 
        }
    }
    return true; 
}
