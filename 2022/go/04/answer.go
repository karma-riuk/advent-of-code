package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Range struct {
	low, high int
}

func (r *Range) contians(other *Range) bool {
	return r.low <= other.low && other.high <= r.high
}

func (r *Range) overlaps(other *Range) bool {
	return (r.low <= other.low && other.low <= r.high) ||
		(r.low <= other.high && other.high <= r.high)
}

func fromString(s string) Range {
	parts := strings.Split(s, "-")
	low, err := strconv.Atoi(parts[0])
	check(err, "Can't convert %q to int", parts[0])
	high, err := strconv.Atoi(parts[1])
	check(err, "Can't convert %q to int", parts[1])
	return Range{low, high}
}

type Input struct {
	ranges []struct{ a, b Range }
}

func input(filename string) *Input {
	file, err := os.Open(filename)
	check(err, "Couldn't open %q", filename)
	defer file.Close()

	input := &Input{}

	scanner := bufio.NewScanner(file)

	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		line := scanner.Text()
		sets := strings.Split(line, ",")
		input.ranges = append(input.ranges, struct{ a, b Range }{fromString(sets[0]), fromString(sets[1])})
	}

	return input
}

func result(inp *Input, part int8) string {
	var res string
	score := 0

	for _, pair := range inp.ranges {
		if part == 1 {
			if pair.a.contians(&pair.b) || pair.b.contians(&pair.a) {
				score++
			}
		} else {
			if pair.a.overlaps(&pair.b) || pair.b.overlaps(&pair.a) {
				score++
			}
		}
	}

	res = fmt.Sprint(score)
	return res
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
