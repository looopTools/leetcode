// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {

        if (n < 2)
        {
            return 1;
        }

        if (n / 2 == 1)
        {
            return firstBad(1, n);
        }   

        int x = n / 2;

        return isBadVersion(x) ? firstBad(1, x) : firstBad(x, n);

    }
private:

    int firstBad(int start, int end)
    {
        for (int i = start; i <= end; ++i)
        {

            if (isBadVersion(i))
            {
                return i;
            }

        }

        return -1;

    }
};
