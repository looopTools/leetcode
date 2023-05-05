/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return add(l1, l2); 
    }

    ListNode* add(ListNode* l1, ListNode* l2, int remainder = 0) 
    {


        if (l1 == nullptr && l2 == nullptr && remainder == 0)
        {
            return nullptr;
        }

        int value = remainder;  

        if (l1 != nullptr)
        {
            value = value + l1->val;
        }

        if (l2 != nullptr)
        {
            value = value + l2->val;
        }

        if (value > 9) 
        {
            remainder = 1;
            value = value - 10; 
        }
        else 
        {
            remainder = 0;
        }

        ListNode* node;
        
        if (l1 != nullptr && l2 != nullptr)
        {
            node = new ListNode(value, add(l1->next, l2->next, remainder));
        }
        else if (l1 == nullptr && l2 != nullptr)
        {
            node = new ListNode(value, add(nullptr, l2->next, remainder));
        }        
        else if (l1 != nullptr && l2 == nullptr)
        {
            node = new ListNode(value, add(l1->next, nullptr, remainder));
        }
        else if (l1 == nullptr && l2 == nullptr)
        {
            node = new ListNode(value, add(nullptr, nullptr, remainder));
        }
         
        return node;


    }
};
