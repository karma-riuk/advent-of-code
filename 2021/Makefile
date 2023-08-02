N=$(shell find ./* -maxdepth 0 -type d | grep -v git | wc -l)
DIR_NAME=$(shell printf "%02d" $(N))

.PHONY: new
new:
	cp -r 00_template "$(DIR_NAME)" && curl -s -H "Cookie: session=$$AOC_SESSION" "https://adventofcode.com/2021/day/$(N)/input" > "$(DIR_NAME)"/input
