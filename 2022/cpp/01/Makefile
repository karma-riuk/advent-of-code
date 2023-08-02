# VERBOSE := 0
CXXFLAGS := -Wall -O3 -DPART=2
OBJ_DIR = build
OBJ = answer.o

.PHONY: clean asdf sample1 sample2

asdf: result
	@echo "------- RESULT -------"
	@./result "input" | xclip -selection c
	@xclip -selection c -o

check: test
	./test

verbose: clean
	$(eval CXXFLAGS += -DVERBOSE)

test: $(OBJ_DIR)/$(OBJ)

sample1 sample2:
	$(eval CXXFLAGS += -DSAMPLE$(@:sample%=%))
	@-rm test

$(OBJ_DIR)/%.o: %.cpp
	@echo "Compiling $<..."
	@mkdir -p $(@D)
	gcc $(CXXFLAGS) -c -o $@ $<

result: $(OBJ_DIR)/$(OBJ)

clean:
	-rm -f *.o
	-rm -rf $(OBJ_DIR)/

