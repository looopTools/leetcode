package main

import "fmt"

func findMaxOccurence(occurenceMap map[int][]byte) int {

	res := -1 
	for key, _ := range occurenceMap {
		if res < key {
			 res = key
		}
	}
	return res
}

func findMinOccurence(occurenceMap map[int][]byte) int {
	res := -1

	for key, _ := range occurenceMap {

		if res == -1 || res > key {
			key = res
		}
	}
	return res
}


func frequencySort(s string) string {

	charMap := make(map[byte]int)
	
	for i := 0; i < len(s); i++ {
		value, exists := charMap[s[i]]
		
		if exists {
			charMap[s[i]] = value + 1
		} else {
			charMap[s[i]] = 1
		}
	}


	orderMap := make(map[int][]byte)

	for key, count := range charMap {
		value, exists := orderMap[count]

		if exists {
			orderMap[count] = append(value, key)
		} else {
			var counts []byte
			orderMap[count] = append(counts, key)
		}
	}

	max := findMaxOccurence(orderMap)
	
	result := []byte{} 



	for i := max; i > 0; i-- {
		chars, exists := orderMap[i] 
		if !exists {
			break;
		} else
		{
			for chr := range chars {
				
				for j := i; j >= 0; j-- {
					result = append(result, chars[chr])
				}
			}
			
		}
		
	}
	
	return string(result)
}

func main() {
	s := "cccaaa"
	fmt.Println(frequencySort(s))

	s = "tree"
	fmt.Println(frequencySort(s))	
}
