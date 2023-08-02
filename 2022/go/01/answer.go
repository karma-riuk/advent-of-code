package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"

	log "github.com/sirupsen/logrus"
)

type Input struct {
	calories [][]int
}

func input(filename string) *Input {
	file, err := os.Open(filename)
	check(err, fmt.Sprintf("Couldn't open %q", filename))
	defer file.Close()

	input := &Input{}
	input.calories = append(input.calories, make([]int, 0))

	scanner := bufio.NewScanner(file)

	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		var line string = scanner.Text()
		if len(line) == 0 {
			input.calories = append(input.calories, make([]int, 0))
		} else {
			cal, err := strconv.Atoi(line)
			check(err, fmt.Sprintf("Couldn't convert %q to int", line))
			input.calories[len(input.calories)-1] = append(input.calories[len(input.calories)-1], cal)
		}
	}

	return input
}

func map_slice[S, T any](ss []S, mapper func(S) T) []T {
	var ret []T = make([]T, 0, len(ss))
	for _, s := range ss {
		ret = append(ret, mapper(s))
	}
	return ret
}

func max(arr []int) int {
	var max int = 0
	for _, e := range arr {
		if e > max {
			max = e
		}
	}
	return max
}

func sum(arr []int) int {
	res := 0
	for _, e := range arr {
		res += e
	}
	return res
}

func result(inp *Input, part int8) string {
	var res string
	if part == 1 {
		var max int = max(
			map_slice(inp.calories, func(s []int) int { return sum(s) }),
		)
		res = fmt.Sprint(max)
	} else {
		sums := map_slice(inp.calories, func(s []int) int { return sum(s) })
		sort.Ints(sums)
		res = fmt.Sprint(sum(sums[len(sums)-3:]))
	}
	return res
}

func check(e error, message string) {
	if e != nil {
		log.Error(message)
		panic(e)
	}
}

func main() {
	fmt.Println(result(input("sample1"), 1))
}
