package main

func searchInsert(nums []int, target int) int {
    if len(nums) == 0 {
        return 0;
    }

    for index, elm := range nums {
        if target <= elm {
            return index;
        }
    }
    
    return len(nums);
}
