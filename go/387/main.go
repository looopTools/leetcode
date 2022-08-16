package main

import "fmt"

type observedPair struct {
	seen int
	firstIndex int
}


func firstUniqChar(s string) int {

	observedMap := make(map[byte]observedPair)
	
	
	for i := 0; i < len(s); i++ {
		val, exists := observedMap[s[i]]
		if !exists {
			pair := observedPair{1, i}
			observedMap[s[i]] = pair
		} else {
			val.seen = val.seen + 1
			observedMap[s[i]] = val
		}
	}

	observedIndex := -1
	
	for _, observed := range observedMap {
		if observed.seen == 1 {
			if observedIndex == -1 || observedIndex > observed.firstIndex {
				observedIndex = observed.firstIndex
			}
		}
	}
	return observedIndex;    
}

func main() {
	fmt.Println(firstUniqChar("abzbaz"));
}
