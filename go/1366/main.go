package main

import "fmt"

func findMax(votes)

func rankTeams(votes []string) string {

	if len(votes) == 0 {
		return "";
	}
	
	if len(votes) == 1 {
		return votes[1]; 
	}

	voteMap := make(map[rune]int);

	for str := range votes {
		for r := range str {
			val, known := voteMap[r];
			if !known {
				voteMap[val] = 1
			} else {
				voteMap[val] = voteMap[val] + 1;
			}
		}
	}

	orderedVoteMap = make(map[int][]rune)

	for r, vote := range voteMap {
		val, known = orderedVoteMap[r];
		if !known {
			
		}
	}
	
	return "";
}

func main() {
	fmt.Println("john"); 
}
