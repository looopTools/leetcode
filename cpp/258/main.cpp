#include <cassert>

class Solution {
public:
    int addDigits(int num) {

        int result = 0;

        while (num != 0) {
            int tmp = num % 10;
            num = (num - tmp) / 10;
            result = result + tmp;
        }

        if (result >= 10) {
            result = addDigits(result);
        }
        return result;
    }
};


int main() {
    Solution s;

    assert(2 == s.addDigits(38));
    assert(0 == s.addDigits(0));
}
