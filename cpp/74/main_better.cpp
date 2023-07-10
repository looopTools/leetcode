class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for (const auto& row : matrix)
        {
            if (*(row.end() - 1) >= target)
            {
                size_t start = 0;
                size_t end = row.size();

                size_t mid = end / 2;
                if (row.at(mid) <= target)
                {
                    start = mid;
                    end = row.size() - 1;
                }
                else
                {
                    end = mid;
                }

                for (; start <= end; ++start)
                {
                    if (row.at(start) == target)
                    {
                        return true;
                    }
                }
            }
            
        }
        return false;
    }
};
