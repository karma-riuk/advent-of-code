COOKIE = 53616c7465645f5fb99dda36ae761920e1f0d561f3761dbaab58f2dcfe046a477f89881d95a683f92a0ac924a6e42c9ab614591a5716915c5de56fe977aa0881

.ONESHELL: 

.PHONY = new create init get_input get_sample
NUMBER := $$(($(shell ls -D | grep "^[0-2][0-9]$$" | wc -l) + 1))
NUMBER_DIR := $(shell printf "%02d" $(NUMBER))
# NUMBER := $(shell ls -D | wc -l)

# https://adventofcode.com/2022/day/1/input

new: create init get_input get_sample

create:
	@echo "Creating $(NUMBER)..."
	@cp -r template/ $(NUMBER_DIR)/

init:
	@echo "Initiliazing go module..."
	@cd $(NUMBER_DIR)
	@rm go.mod
	@go mod init aoc/$(NUMBER)
	@go mod tidy

get_input:
	@echo "Getting input..."
	@wget -q -O $(NUMBER_DIR)/input --header "Cookie: session=$(COOKIE)" https://adventofcode.com/2022/day/$(NUMBER)/input

get_sample:
	@echo "Getting sample... Is it in your clipboard? I surely hope so..."
	@xclip -o > $(NUMBER_DIR)/sample1
