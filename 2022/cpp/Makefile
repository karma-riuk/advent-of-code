COOKIE = 53616c7465645f5f49dff2a6091a00e67a9678384d5d9867c24d2c2024c8524adb2391b31b45118c978505c7ea27ddecf0cc047ce8d51dc32203dffde652c690

.PHONY = new
NUMBER := $$(($(shell ls -D | grep "^[0-2][0-9]$$" | wc -l) + 1))
NUMBER_DIR := $(shell printf "%02d" $(NUMBER))
# NUMBER := $(shell ls -D | wc -l)

# https://adventofcode.com/2022/day/1/input

new:
	@echo "Creating $(NUMBER)..."
	cp -r template/ $(NUMBER_DIR)/
	@echo "Getting input"
	@wget -q -O $(NUMBER_DIR)/input --header "Cookie: session=$(COOKIE)" https://adventofcode.com/2022/day/$(NUMBER)/input
	sed -i "s/DATE/$(NUMBER_DIR)/" $(NUMBER_DIR)/answer.cpp
	xclip -o > $(NUMBER_DIR)/sample1
