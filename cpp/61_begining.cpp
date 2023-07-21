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
    int len(ListNode* head) const
    {
        ListNode* current = head; 
        int length = 0; 
        while(current != nullptr)
        {
            length = length + 1; 
            current = current->next; 
        }
        return length;
    }

    void get_tail(ListNode* head, ListNode* new_tail, ListNode* tail)
    {
        ListNode* current = head;  
        while(current->next->next != nullptr)
        {
            current = current->next;
        }
        tail = current->next; 
        new_tail = current; 
    }



public:
    ListNode* rotateRight(ListNode* head, int k) {
        

        auto length = len(head);

        if (length == 0 || length == 1)
        {
            return head; 
        }
        //std::cout << (length - 1) << "\n"; 
        for (int i = 0; i < k; ++i)
        {
            ListNode* current = head;  
            while(current->next->next != nullptr)
            {
                current = current->next;
            }

            current->next->next = head; 
            head = current->next;
            current->next = nullptr;
        }
        return head;
    }
};
