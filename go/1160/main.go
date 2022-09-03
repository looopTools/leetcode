package main

import "fmt"

func frequencyMap(chars string) map[rune]int {

	frequency := make(map[rune]int)
	
	for _, elm := range chars {
		value, exists := frequency[elm]

		if exists {
			frequency[elm] = value + 1
		} else {
			frequency[elm] = 1
		}
	}

	return frequency 
}

func countCharacters(words []string, chars string) int {
	count := 0;

	charsFrequencyMap := frequencyMap(chars)
	
	for _, word := range words {

		wordFrequencyMap := frequencyMap(word)
		
		accepted := true;
		
		for _, chr := range word {
			_, exists := charsFrequencyMap[chr]

			if !exists || (exists && charsFrequencyMap[chr] < wordFrequencyMap[chr]) {
				accepted = false
				break;				
			} 
		}

		if accepted {
			count = count + len(word);
		}
	}
	return count;
}

func main() {

	words := []string{"cat","bt","hat","tree"};
	chars := "atach";	
	fmt.Println(countCharacters(words, chars));

	words = []string{"hello","world","leetcode"};
	chars = "welldonehoneyr";
	fmt.Println(countCharacters(words, chars));

	words = []string{"dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin","ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb","ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl","boygirdlggnh","xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx","nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop","hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx","juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr","lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo","oxgaskztzroxuntiwlfyufddl","tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp","qnagrpfzlyrouolqquytwnwnsqnmuzphne","eeilfdaookieawrrbvtnqfzcricvhpiv","sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz","yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue","hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv","cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo","teyygdmmyadppuopvqdodaczob","qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs","qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"}

	chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp";
	fmt.Println(countCharacters(words, chars));
	
	

	
}
