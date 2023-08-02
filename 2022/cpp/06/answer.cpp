// AOC - 2022 - 06
#include "answer.hpp"

#include <algorithm>
#include <deque>
#include <fstream>
#include <iostream>
#include <queue>
#include <unordered_set>

Input get_input(const char* filename) {
    std::ifstream stream(filename);
    std::string str;
    getline(stream, str);
    return {str};
}

template <class T>
bool contains_duplicates(std::deque<T> q) {
    std::unordered_set<T> set;
    for (auto& elem : q) {
        if (set.find(elem) != set.end())
            return true;
        set.insert(elem);
    }
    return false;
}

std::string get_result(Input input) {
    std::string ret;
    std::stringstream stream(input.str);
    std::deque<char> q;
    char c;
#if PART == 1
#define Q_SIZE 4
#else
#define Q_SIZE 14
#endif
    for (int i = 0; i < Q_SIZE - 1; i++) {
        stream >> c;
        q.push_back(c);
    }

    int i = Q_SIZE - 1;
    while (stream.rdbuf()->in_avail()) {
        i++;
        stream >> c;
        q.push_back(c);
        if (!contains_duplicates(q)) {
            std::cout << q << "is duplicate free" << std::endl;
            break;
        }
        std::cout << q << " DOES contain duplicates" << std::endl;
        q.pop_front();
    }
    ret = std::to_string(i);
    return ret;
}
