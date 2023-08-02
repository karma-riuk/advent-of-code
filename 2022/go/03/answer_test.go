package main

import (
	"reflect"
	"testing"
)

func TestPriority(t *testing.T) {
	tests := []struct {
		c        rune
		expected int
	}{
		{'a', 1},
		{'b', 2},
		{'p', 16},
		{'L', 38},
		{'P', 42},
		{'v', 22},
		{'t', 20},
		{'s', 19},
	}

	for _, test := range tests {
		var got int = priority(test.c)

		if got != test.expected {
			t.Errorf("priority(%q) = %v, want %v", test.c, got, test.expected)
		}
	}
}

func TestInputSample1(t *testing.T) {
	filename := "sample1"
	expected := &Input{
		sacks: []Sack{
			{"vJrwpWtwJgWr", "hcsFMMfFFhFp"},
			{"jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"},
			{"PmmdzqPrV", "vPwwTWBwg"},
			{"wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn"},
			{"ttgJtRGJ", "QctTZtZT"},
			{"CrZsJsPPZsGz", "wwsLwLmpwMDw"},
		},
	}
	var got *Input = input(filename)

	if !reflect.DeepEqual(expected, got) {
		t.Errorf("input(%q) = %v, want %v", filename, got, expected)
	}
}

func TestResult(t *testing.T) {
	tests := []struct {
		part     int8
		filename string
		expected string
	}{
		{1, "sample1", "157"},
		{1, "input", "7727"},

		{2, "sample1", "70"},
		{2, "input", "2609"},
	}

	for _, test := range tests {
		var got string = result(input(test.filename), test.part)

		if got != test.expected {
			t.Errorf("result = %q, want %q", got, test.expected)
		}
	}
}
