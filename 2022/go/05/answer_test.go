package main

import (
	"reflect"
	"testing"
)

func TestInputSample1(t *testing.T) {
	filename := "sample1"
	expected := &Input{
		stacks: []Stack{
			{'Z', 'N'},
			{'M', 'C', 'D'},
			{'P'},
		},
		moves: []Move{
			{1, 2, 1},
			{3, 1, 3},
			{2, 2, 1},
			{1, 1, 2},
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
		{1, "sample1", "CMZ"},
		{1, "input", "TDCHVHJTG"},

		{2, "sample1", "MCD"},
		{2, "input", "NGCMPJLHV"},
	}

	for _, test := range tests {
		var got string = result(input(test.filename), test.part)

		if got != test.expected {
			t.Errorf("result = %q, want %q", got, test.expected)
		}
	}
}
