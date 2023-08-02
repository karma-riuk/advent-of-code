// AOC - 2022 - 08
#include "answer.hpp"

#include <fstream>
#include <iostream>
#include <string>

Input get_input(const char* filename) {
    std::ifstream stream(filename);
    std::string str;
    Input ret;

    getline(stream, str);
    ret.width = str.size();
    for (auto c : str)
        ret.trees.push_back(c);

    while (getline(stream, str))
        for (char c : str)
            ret.trees.push_back(c);
    ret.height = ret.trees.size() / ret.width;
    return ret;
}

bool is_tree_seen(uint x, uint y, Forest& forest) {
    Tree current_tree = forest.tree_at(x, y);
    bool is_seen = true;
    // north
    for (uint i = 0; i < y; i++)
        if (forest.tree_at(x, i) >= current_tree)
            is_seen = false;
    if (is_seen)
        return true;

    is_seen = true;
    // east
    for (uint i = x + 1; i < forest.width; i++)
        if (forest.tree_at(i, y) >= current_tree)
            is_seen = false;
    if (is_seen)
        return true;

    is_seen = true;
    // south
    for (uint i = y + 1; i < forest.height; i++)
        if (forest.tree_at(x, i) >= current_tree)
            is_seen = false;
    if (is_seen)
        return true;

    is_seen = true;
    // west
    for (uint i = 0; i < x; i++)
        if (forest.tree_at(i, y) >= current_tree)
            is_seen = false;

    if (!is_seen)
        std::cout << "couldn't see tree " << current_tree << " at " << x << ", "
                  << y << std::endl;

    return is_seen;
}

uint scenic_score(uint x, uint y, Forest& forest) {
    Tree current_tree = forest.tree_at(x, y);
    uint total_score = 1;
    uint score = 0;

    // north
    for (int i = y - 1; i >= 0; i--) {
        score++;
        if (forest.tree_at(x, i) >= current_tree)
            break;
    }
    total_score *= score;

    score = 0;
    // east
    for (uint i = x + 1; i < forest.width; i++) {
        score++;
        if (forest.tree_at(i, y) >= current_tree)
            break;
    }
    total_score *= score;

    score = 0;
    // south
    for (uint i = y + 1; i < forest.height; i++) {
        score++;
        if (forest.tree_at(x, i) >= current_tree)
            break;
    }
    total_score *= score;

    score = 0;
    // west
    for (int i = x - 1; i >= 0; i--) {
        score++;
        if (forest.tree_at(i, y) >= current_tree)
            break;
    }

    total_score *= score;

    return total_score;
}

std::string get_result(Input& forest) {
    std::string ret;
#if PART == 1
    uint count = 2 * forest.width + 2 * forest.height - 4;
    for (uint y = 1; y < forest.height - 1; y++) {
        for (uint x = 1; x < forest.width - 1; x++)
            if (is_tree_seen(x, y, forest))
                count++;
    }
    ret = std::to_string(count);
#else
    uint max_scenic_score = 0;
    for (uint y = 1; y < forest.height - 1; y++) {
        for (uint x = 1; x < forest.width - 1; x++) {
            uint score = scenic_score(x, y, forest);
            if (max_scenic_score < score)
                max_scenic_score = score;
        }
    }
    ret = std::to_string(max_scenic_score);
#endif
    return ret;
}
