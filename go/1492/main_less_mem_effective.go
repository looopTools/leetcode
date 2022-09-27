package main

import "fmt"

func kthFactor(n int, k int) int {

	var factors []int; 

	for i := 1; i <= n; i++ {
		if (n % i == 0) {
			factors = factors.append(factors, i); 
		}
	}

	if (len(factors) < k) {
		return -1; 
	}
	return factors[k - 1]; 
}


func main() {
	fmt.Println("kth Factor: ", kthFactor(12, 3));
}
