package main

import "fmt"

func percentageLetter(s string, letter byte) int {

	strLen := len(s)
	letterKnown := 0

	for i := 0; i < len(s); i++ {
		if s[i] == letter {
			letterKnown = letterKnown + 1
		}
	}

	if letterKnown == 0 {
		return 0
	}

	return int((float64(letterKnown) / float64(strLen)) * 100);	
}

func main() {

	s := "foobar"
	fmt.Println(percentageLetter(s, 'o'))

	s = "jjjjj"
	fmt.Println(percentageLetter(s, 'k'))	
	
}
