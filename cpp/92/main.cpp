#include <iostream>


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        
        //left = 0;
        
        //left = left == 0 ? left : left -1; 
        //right = right -1; 
        while(left < right)
        {
            int rhs_new = (head + (left + 1))->val;
            int lhs_new = (head + right + 1)->val;

            std::cout << std::to_string(rhs_new) << "\n";

            (head + left)->val = lhs_new;
            (head + right)->val = rhs_new;

            left = left + 1;
            right = right - 1;

        }

        return head;
    }

    void print(ListNode* head)
    {
        ListNode* node = head;
        std::cout << "[";
        while(node->next != nullptr)
        {
            std::cout << std::to_string(node->val) <<", ";
            node = node->next;
        }

        std::cout << std::to_string(node->val) << "]\n";

        
    }
};


int main(void)
{

    ListNode* five = new ListNode(5);
    ListNode* four = new ListNode(4, five);
    ListNode* three = new ListNode(3, four);
    ListNode* two = new ListNode(2, three);
    ListNode* one = new ListNode(1, two);

    Solution s;
    s.print(one);
    one = s.reverseBetween(one, 2, 4);
    s.print(one);    
}
