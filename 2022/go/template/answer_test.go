package main

import (
	"reflect"
	"testing"
)

func TestInputSample1(t *testing.T) {
	filename := "sample1"
	expected := &Input{}
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
		{1, "sample1", ""},
		{1, "input", ""},

		// {2, "sample1", ""},
		// {2, "input", ""},
	}

	for _, test := range tests {
		var got string = result(input(test.filename), test.part)

		if got != test.expected {
			t.Errorf("result = %q, want %q", got, test.expected)
		}
	}
}
