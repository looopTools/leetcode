# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return None
        
        if head.next == None:
            return head

        previous = head
        current = head.next

        while current != None:
            
            if current.val != previous.val:
                previous.next = current
                previous = current
            current = current.next
            
        previous.next = None
        
        return head        

def print_nodes(head):

    current = head

    str = ""
    while current:
        str = f"{str}{current.val} "
        current = current.next
    print(f"[{str}]")

def test_case_one(solution):

    print(" ")
    print("Running Test case One")
    sorted_list = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2)))
    print_nodes(solution.deleteDuplicates(sorted_list))

def test_case_two(solution):

    print(" ")
    print("Running Test case 2")
    sorted_list = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=3)))))
    print_nodes(solution.deleteDuplicates(sorted_list))




if __name__ == "__main__":

    solution = Solution()
    print("Running Code")
    test_case_one(solution)
    test_case_two(solution)
    
    
