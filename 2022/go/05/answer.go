package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Stack []byte

func (s *Stack) String() string {
	var res strings.Builder

	for _, crate := range *s {
		res.WriteByte(crate)
		res.WriteString(" ")
	}
	return res.String()
}

func (s *Stack) isEmpty() bool {
	return len(*s) == 0
}

func (s *Stack) push(t ...byte) {
	*s = append(*s, t...)
}

func (s *Stack) pop(n int) ([]byte, error) {
	if s.isEmpty() {
		return nil, errors.New("Couldn't pop from empty stack")
	}
	index := len(*s) - n
	ret := (*s)[index:]
	*s = (*s)[:index]
	return ret, nil
}

type Move struct {
	n, from, to int
}

type Input struct {
	stacks []Stack
	moves  []Move
}

func input(filename string) *Input {
	file, err := os.Open(filename)
	check(err, "Couldn't open %q", filename)
	defer file.Close()

	input := &Input{}

	scanner := bufio.NewScanner(file)

	scanner.Split(bufio.ScanLines)

	var n_stacks int = 0

	// Parse the stacks
	for scanner.Scan() {
		line := scanner.Text()

		if line[1] == '1' {
			break
		}

		if len(input.stacks) == 0 {
			n_stacks = (len(line) + 1) / 4
			input.stacks = make([]Stack, n_stacks)
		}

		for i := 0; i < n_stacks; i++ {
			crate := line[4*i+1]
			if crate != ' ' {
				input.stacks[i].push(crate)
			}
		}
	}

	// Reverse the stacks since they were added top-down and not bottom-up
	for _, stack := range input.stacks {
		for i, j := 0, len(stack)-1; i < j; i, j = i+1, j-1 {
			stack[i], stack[j] = stack[j], stack[i]
		}
	}

	scanner.Scan() // get rid of the empty line after the labeling of the stacks

	// Parse the moves
	for scanner.Scan() {
		line := scanner.Text()
		tokens := strings.Split(line, " ")

		n, err := strconv.Atoi(tokens[1])
		check(err, "Couldn't convert %q to int", tokens[1])
		from, err := strconv.Atoi(tokens[3])
		check(err, "Couldn't convert %q to int", tokens[3])
		to, err := strconv.Atoi(tokens[5])
		check(err, "Couldn't convert %q to int", tokens[5])

		input.moves = append(input.moves, Move{
			n:    n,
			from: from,
			to:   to,
		})
	}

	return input
}

func result(inp *Input, part int8) string {
	var res strings.Builder

	for _, move := range inp.moves {
		moving, err := inp.stacks[move.from-1].pop(int(move.n))
		check(err, "ntm")
		if part == 1 {
			for i, j := 0, len(moving)-1; i < j; i, j = i+1, j-1 {
				moving[i], moving[j] = moving[j], moving[i]
			}
		}

		inp.stacks[move.to-1].push(moving...)
	}

	for _, stack := range inp.stacks {
		log.Print(stack.String())
		res.WriteByte(stack[len(stack)-1])
	}

	return res.String()
}

func check(e error, msg string, vals ...any) {
	if e != nil {
		log.Printf("ERROR: "+msg, vals)
		panic(e)
	}
}

func main() {
	result := result(input("sample1"), 1)

	log.Println(result)
	fmt.Println(result)
}
