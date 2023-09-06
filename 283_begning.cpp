class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        int step = 0; 
        size_t index = 0; 

        while(step != nums.size())
        {
            if (*(nums.begin() + index) == 0)
            {
                nums.erase(nums.begin() + index);
                nums.push_back(0); 
            }
            else
            {   
                index = index + 1; 
            }

            step = step + 1;
        }
    }
};
