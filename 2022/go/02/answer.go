package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

const (
	ROCK int = iota
	PAPER
	SCISSOR
)

const (
	LOSS int = 3 * iota
	DRAW
	WIN
)

type Turn struct {
	them int
	me   int
}
type Input struct {
	turns []Turn
}

var str_to_RPS = map[string]int{
	"A": ROCK,
	"B": PAPER,
	"C": SCISSOR,

	"X": ROCK,
	"Y": PAPER,
	"Z": SCISSOR,
}

func input(filename string) *Input {
	file, err := os.Open(filename)
	check(err)
	defer file.Close()

	input := &Input{
		turns: []Turn{},
	}

	scanner := bufio.NewScanner(file)

	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		line := scanner.Text()
		hands := strings.Split(line, " ")
		input.turns = append(input.turns, Turn{str_to_RPS[hands[0]], str_to_RPS[hands[1]]})
	}

	return input
}

func result(inp *Input, part int8) string {
	var res string
	score := 0
	for _, turn := range inp.turns {
		score += turn.me + 1
		if turn.me == (turn.them+1)%3 {
			score += WIN
		} else if turn.me == turn.them {
			score += DRAW
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
	log.SetFlags(log.Lshortfile)

	log.Println(result)
	fmt.Println(result)
}
