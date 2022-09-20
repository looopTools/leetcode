package main

import "fmt";
 
type ListNode struct {
      Val int
      Next *ListNode
}


func swap(lhs *ListNode, rhs *ListNode) *ListNode{
	lhs.Next = rhs.Next;
	rhs.Next = lhs.Next;
	return rhs;
}


func swapPairs(head *ListNode) *ListNode {



	if (head.Next == nil) {
		return head;
	}

	isHead := false;

	lhs := head;

	
	for (lhs.Next != nil) {
		lhs = swap(lhs, lhs.Next);
		if isHead {
			head = lhs;
			isHead = false;
		}
		lhs = lhs.Next;
	}
	
	return head; 
	
}

func Print(node *ListNode) {

	for (node != nil) {
		fmt.Println(node.Val, " ");
		node = node.Next;
	}
}

func main() {

	var n4 ListNode
	n4.Val = 4;
	n4.Next = nil;

	var n3 ListNode
	n3.Val = 3;
	n3.Next = &n4;

	var n2 ListNode
	n2.Val = 2;
	n2.Next = &n3;

	var n1 ListNode
	n1.Val = 1;
	n1.Next = &n2;
	//Print(&n1);

	n6 := swapPairs(&n1);
	Print(n6);


}
