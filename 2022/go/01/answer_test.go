package main

import (
	"reflect"
	"testing"
)

func TestInputSample1(t *testing.T) {
	filename := "sample1"
	expected := &Input{
		calories: [][]int{
			{1000, 2000, 3000},
			{4000},
			{5000, 6000},
			{7000, 8000, 9000},
			{10000},
		},
	}
	var got *Input = input(filename)

	if !reflect.DeepEqual(*got, *expected) {
		t.Errorf("input(%q) = %v, want %v", filename, got, expected)
	}
}

func TestResult(t *testing.T) {
	tests := []struct {
		part     int8
		filename string
		expected string
	}{
		{1, "sample1", "24000"},
		{1, "input", "71924"},
		{2, "sample1", "45000"},
		{2, "input", "210406"},
	}
	for _, test := range tests {
		var got string = result(input(test.filename), test.part)

		if got != test.expected {
			t.Errorf("result = %q, want %q", got, test.expected)
		}
	}
}
