package main
import "fmt"

func edgeScore(edges []int) int {

	node := -1
	score := -1
	
	scoreMap := make(map[int]int)

	for i := 0; i < len(edges); i++ {
		value, exists := scoreMap[edges[i]]

		if exists {
			scoreMap[edges[i]] = value + i
		} else {
			scoreMap[edges[i]] = i
		}

		if score < scoreMap[edges[i]] {
			node = edges[i]
			score = scoreMap[edges[i]]
		} else if score == scoreMap[edges[i]] && edges[i] < node {
			node = edges[i]
		
		}
	}

	return node
}

func main() {
	edges := []int{1,0,0,0,0,7,7,5}
	
	fmt.Println("Edge Score: ", edgeScore(edges))

	edges = []int{2,0,0,2}
	
	fmt.Println("Edge Score: ", edgeScore(edges))	
}
