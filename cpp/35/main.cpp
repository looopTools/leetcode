class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.empty())
        {
            return 0;
        }

        for (int i = 0; i < nums.size(); ++i)
        {

            if (target <= nums.at(i))
            {
                return i;
            }
        }

        return nums.size();
    }
};
