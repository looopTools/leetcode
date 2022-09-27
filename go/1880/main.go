package main

import "fmt"

func getSum (word string) int {

	sum := 0;

	for i := 0; i < len(word); i++ {
		sum = (sum * 10) + (int(word[i]) - 97); 
	}
	return sum;  
}

func isSumEqual(firstWord string, secondWord string, targetWord string) bool {

	return (getSum(firstWord) + getSum(secondWord)) == getSum(targetWord); 
}

func main () {

	fmt.Println("Is sum equal: ", isSumEqual("acb", "cba", "cdb"));
	fmt.Println("Is sum equal: ", isSumEqual("aaa", "a", "aab"));
	fmt.Println("Is sum equal: ", isSumEqual("aaa", "a", "aaaa")); 
}
