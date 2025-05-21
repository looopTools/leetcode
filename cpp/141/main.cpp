
#include <map>
#include <cstdint>
#include <cassert>

#include <iostream>
// Definition for singly-linked list.
  struct ListNode {
      int val;
      ListNode* next;
      ListNode(int x) : val(x), next(NULL) {}
  };


class Solution {
public:
    bool hasCycle(ListNode *head) {
        std::map<uintptr_t, bool> visited;

        ListNode* current = head;
        while (current != NULL) {
            auto addr = reinterpret_cast<uintptr_t>(current);
            if (visited.contains(addr)) {
                return true;
            }
            else {
                visited[addr] = true;
            }
            current = current->next;
        }
        return false;
    }
};

class SolutionTwo {

public:
    bool hasCycle(ListNode *head) {
        ListNode* current = head;
        auto prev = reinterpret_cast<uintptr_t>(head);

        while (current != NULL) {
            auto addr = reinterpret_cast<uintptr_t>(current);

            if (prev < addr) {
                return true;
            }

            prev = addr;
            current = current->next;
        }
        return false;
    }
};

int main() {

    auto one = ListNode(3);
    // auto two = ListNode(2);
    // one.next = &two;
    // auto three = ListNode(0);
    // two.next = &three;
    // auto four = ListNode(-4);
    // three.next = &four;
    // four.next = &two;

    SolutionTwo s;
    assert(false == s.hasCycle(&one));
}
