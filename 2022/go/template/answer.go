package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type Input struct{}

func input(filename string) *Input {
	file, err := os.Open(filename)
	check(err, "Couldn't open %q", filename)
	defer file.Close()

	input := &Input{}

	scanner := bufio.NewScanner(file)

	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		line := scanner.Text()
	}

	return input
}

func result(inp *Input, part int8) string {
	var res string

	if part == 1 {
	} else {
	}

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
