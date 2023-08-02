// AOC - 2022 - 05
#include "answer.hpp"
#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>

#define STACK_WIDTH 4

stacks_t get_stacks(std::vector<std::string> stack_lines, uint n_stacks) {
    // reverse so that stack_lines[0] is the bottom of the stacks
    std::reverse(stack_lines.begin(), stack_lines.end());

    std::vector<std::vector<char>> stacks(n_stacks);
    uint max_height = stack_lines.size();

    for (uint h = 0; h < max_height; h++) {
        for (uint i = 0; i < n_stacks; i++) {
            char item = stack_lines[h][i * STACK_WIDTH + 1];
            if (item != ' ')
                stacks[i].push_back(item);
        }
    }
    return stacks;
}

Move get_move(std::string line) {
    std::stringstream ss(line);
    std::string _;
    uint item, from, to;
    ss >> _; // move
    ss >> item;
    ss >> _; // from
    ss >> from;
    ss >> _; // to
    ss >> to;
    return {--item, --from, --to};
}

Input get_input(const char * filename) {
    std::ifstream stream(filename);
    std::string str;
    Input ret;

    std::vector<std::string> stack_lines;
    stacks_t stacks;

    while (getline(stream, str) && !std::isdigit(str[1])) {
        stack_lines.push_back(str);
    }
    std::reverse(str.begin(), str.end() - 1);
    std::stringstream ss(str);
    uint n_stacks;
    ss >> n_stacks;
    stacks = get_stacks(stack_lines, n_stacks);

    getline(stream, str); // get rid of the empty line between the stacks and
                          // the move instructions

    std::vector<Move> moves;
    while (getline(stream, str))
        moves.push_back(get_move(str));

    return {stacks, moves};
}

template <class T> std::vector<T> pop(std::vector<T> & v, uint i) {
    std::vector<T> ret(v.begin() + i, v.end());
    v.erase(v.begin() + i, v.end());
    return ret;
}

std::string get_result(Input input) {
    std::string ret;
    stacks_t stacks = input.stacks;
    std::cout << stacks << std::endl;
    for (auto & move : input.moves) {
        std::cout << move << std::endl;
        std::vector<char> tbi = pop(stacks[move.from], stacks[move.from].size() - 1 - move.item);
#if PART == 1
        std::reverse(tbi.begin(), tbi.end());
#endif
        stacks[move.to].insert(stacks[move.to].end(),
                               tbi.begin(), tbi.end());
        std::cout << stacks << std::endl << std::endl;
    }

    for (auto & stack : stacks)
        ret += stack.back();
    return ret;
}
