import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if not head:
            return head

        result = None
        current = head
        prev = None

        while current != None:

            if current.val != val:
                if result is None:
                    result = current

                if prev is None:
                    prev = current
                else:
                    prev.next = current
                    prev = current
                current = current.next
                prev.next = None
            else:
                current = current.next
                
        return result 
        
            
            
class TestRemoveElements(unittest.TestCase):

    def testRemoveElements(self):

        solution = Solution()
        input = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=6, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=ListNode(val=6)))))))
        expected = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
        result = solution.removeElements(input, 6)
        
        self.assertTrue(self.__are_same(result, expected))

        input = ListNode(val=7, next=ListNode(val=7, next=ListNode(val=7, next=ListNode(val=7))))
        expected = None
        result = solution.removeElements(input, 7)
        
        self.assertTrue(self.__are_same(result, expected))

        input = None
        expected = None
        result = solution.removeElements(input, 1)
        
        self.assertTrue(self.__are_same(result, expected))                

    def __are_same(self, lhs, rhs):

        while not lhs is None and not rhs is None:
            if lhs.val != lhs.val:
                return False
            lhs = lhs.next
            rhs = rhs.next
        return lhs is None and rhs is None

    def __print(self, lst):

        str = ""
        while lst is not None:
            str = f"{str}{lst.val} "
            lst = lst.next
        print(f'[{str}]')

if __name__ == "__main__":
    unittest.main()
