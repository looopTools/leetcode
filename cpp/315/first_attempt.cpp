class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        
        if (nums.empty())
        {
            return nums;
        }
        
        for (size_t i = 0; i < nums.size(); ++i)
        {
            int less = 0;
            for (size_t j = i + 1; j < nums.size(); ++j)
            {
                if (nums[i] > nums[j])
                {
                    less = less + 1;
                }
            }
            nums[i] = less;
        }
        return nums;
        
    }
};
