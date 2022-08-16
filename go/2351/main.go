package main 
import "fmt"

func repeatedCharacter(s string) byte {
	observed := make(map[byte]int)

	for i := 0; i < len(s); i++ {
		_, exists := observed[s[i]]
		if !exists {
			observed[s[i]] = 1
		} else {
			return s[i]
		}
	}
	return 0
	
}

func main() {
	fmt.Println(string(repeatedCharacter("abccbaacz")))
}
