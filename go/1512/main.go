package main

import "fmt"

func numIdenticalPairs(nums []int) int {

	numOfIdenticalPairs := 0;
	
	for i := 0; i < len(nums) - 1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] == nums[j] {
				numOfIdenticalPairs = numOfIdenticalPairs + 1; 
			}
		}
	}

	return numOfIdenticalPairs; 
}

func main() {

	nums := []int {1, 2, 3, 1, 1, 3};
	fmt.Println(numIdenticalPairs(nums)); 
}
