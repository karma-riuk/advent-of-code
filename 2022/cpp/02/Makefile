PART := 1
CXXFLAGS := -Wall -O3 -DPART=$(PART)
OBJ_DIR = build
OBJ = answer.o

.PHONY = clean asdf sample1 sample2

asdf: result
	@echo "------- RESULT -------"
	@./result "input" | xclip -selection c
	@xclip -selection c -o

check: test
	./test

test: $(OBJ_DIR)/$(OBJ)

verbose: clean
	$(eval CXXFLAGS += -DVERBOSE)

# sample1 sample2: $(OBJ_DIR)/$(OBJ)
	# $(eval CXXFLAGS += -DSAMPLE$(@:sample%=%))

$(OBJ_DIR)/$(OBJ): $(OBJ_DIR)/%.o: %.hpp

$(OBJ_DIR)/%.o: %.cpp
	@echo "Compiling $<..."
	@mkdir -p $(@D)
	gcc $(CXXFLAGS) -c -o $@ $<

result: $(OBJ_DIR)/$(OBJ)

clean:
	-rm -f *.o
	-rm -rf $(OBJ_DIR)/

