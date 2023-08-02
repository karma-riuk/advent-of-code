package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type Sack struct {
	first  string
	second string
}
type Input struct {
	sacks []Sack
}

func input(filename string) *Input {
	file, err := os.Open(filename)
	check(err)
	defer file.Close()

	input := &Input{
		sacks: []Sack{},
	}

	scanner := bufio.NewScanner(file)

	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		line := strings.Trim(scanner.Text(), "\n")
		input.sacks = append(input.sacks, Sack{
			line[:len(line)/2],
			line[len(line)/2:],
		})
	}

	return input
}

func priority(c rune) int {
	score := 0
	if c >= 'a' && c <= 'z' {
		score += int(c-'a') + 1
	} else if c >= 'A' && c <= 'Z' {
		score += int(c-'A') + 27
	}
	return score
}

func result(inp *Input, part int8) string {
	var res string

	score := 0
	if part == 1 {
		for _, sack := range inp.sacks {
			for _, char := range sack.first {
				if strings.Contains(sack.second, string(char)) {
					score += priority(char)
					break
				}
			}
		}
	} else {
		for i := 0; i < len(inp.sacks); i += 3 {
			sack := inp.sacks[i]
			for _, char := range sack.first + sack.second {
				if strings.Contains(inp.sacks[i+1].first+inp.sacks[i+1].second, string(char)) &&
					strings.Contains(inp.sacks[i+2].first+inp.sacks[i+2].second, string(char)) {
					score += priority(char)
					break
				}
			}
		}
	}

	res = fmt.Sprint(score)

	return res
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	result := result(input("sample1"), 1)

	log.Println(result)
	fmt.Println(result)
}
