#include <map>

class Solution
{
public:
    int fib(int n)
    {
        std::map<int, int> mem;
        return fib(n, mem);
    }

    int fib2(int n)
    {
        if (n == 0 || n == 1)
        {
            return n;
        }
        
        int previous = 0;
        int current = 1;
        int i = 2;

        int tmp = 0;
        while (i <= n)
        {
            tmp = previous + current;
            previous = current;
            current = tmp;
            i++;
        }
        return current;
            
    }

private:

    int fib(int n, std::map<int, int>& mem)
    {
        if (n == 0 || n == 1)
        {
            return n;
        }
        
        if (mem.contains(n))
        {
            return mem[n];
        }

        mem[n] = fib(n - 2, mem) + fib(n - 1, mem);
        return mem[n];
    }
};


#include <iostream>

int main(void)
{
    Solution s;
    std::cout << s.fib(4) << "\n";
    std::cout << s.fib2(4) << "\n";    
}
