class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for (const auto& row : matrix)
        {
            if (*(row.end() - 1) >= target)
            {
                for (const auto& col : row)
                {
                    if (col == target)
                    {
                        return true;
                    }
                }
            }
            
        }
        return false;
    }
