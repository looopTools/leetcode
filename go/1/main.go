package main

import "fmt"

// O(n) solution shold be possible to improve
func twoSum(nums []int, target int) []int {

	res := make([]int, 2)
	for i := 0; i < len(nums) - 1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] + nums[j]  == target {
				res[0] = i
				res[1] = j
			}
 		}
	}
	return res
}

func main() {
	a := []int{2, 7,11,15}
	fmt.Println("Test:", twoSum(a, 9))
}



