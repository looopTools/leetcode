package main

import "fmt"

func kthFactor(n int, k int) int {

	var factor int = 0;
	var kth int = 0; 

	for i := 1; i <= n; i++ {
		if (n % i == 0) {
			factor = i
			kth = kth + 1
			if (kth == k) {
				return factor; 
			}
		}
	}
	return -1; 
}


func main() {
	fmt.Println("kth Factor: ", kthFactor(12, 3));
}
