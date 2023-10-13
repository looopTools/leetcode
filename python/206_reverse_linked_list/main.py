# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        previous = None
        current = head
        

        while current != None:
            if not previous:
                previous = current
                current = current.next
                previous.next = None
            else:
                tmp = current.next
                current.next = previous
                previous = current
                current = tmp
        head = previous 
        return head

def print_list(node):

    str = ""
    
    while node:
        str = f"{str}{node.val} "
        node = node.next
    print(str)
    
def test_case_one():
    l  = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Testing with list")
    print_list(l)

    s = Solution()
    l = s.reverseList(l)
    print_list(l)

def test_case_two():
    l  = ListNode(1, ListNode(2))
    print("Testing with list")
    print_list(l)

    s = Solution()
    l = s.reverseList(l)

    print_list(l)

def test_case_three():
    l  = None
    print("Testing with list")
    print_list(l)

    s = Solution()
    l = s.reverseList(l)
    print_list(l)

if __name__ == "__main__":

    test_case_one()
    test_case_two()
    test_case_three()
