package main

import (
	"reflect"
	"testing"
)

func TestInputSample1(t *testing.T) {
	filename := "sample1"
	expected := &Input{
		ranges: []struct{ a, b Range }{
			{Range{2, 4}, Range{6, 8}},
			{Range{2, 3}, Range{4, 5}},
			{Range{5, 7}, Range{7, 9}},
			{Range{2, 8}, Range{3, 7}},
			{Range{6, 6}, Range{4, 6}},
			{Range{2, 6}, Range{4, 8}},
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
		{1, "sample1", "2"},
		{1, "input", "530"},

		{2, "sample1", "4"},
		{2, "input", "903"},
	}

	for _, test := range tests {
		var got string = result(input(test.filename), test.part)

		if got != test.expected {
			t.Errorf("result = %q, want %q", got, test.expected)
		}
	}
}
