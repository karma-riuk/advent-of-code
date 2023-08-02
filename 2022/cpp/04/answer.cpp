// AOC - 2022 - 04
#include "answer.hpp"
#include <fstream>
#include <iostream>
#include <sstream>

Range get_range(std::stringstream & ss) {
    uint start, end;
    char _;
    ss >> start;
    ss >> _;
    ss >> end;
    ss >> _;
    return {start, end};
}

std::vector<Input> get_input(const char * filename) {
    std::ifstream stream(filename);
    std::string str;
    std::vector<Input> ret;

    while (getline(stream, str)) {
        std::stringstream ss(str);
        ret.push_back({get_range(ss), get_range(ss)});
    }
    return ret;
}

bool Range::fully_contains(const Range & rhs) const {
    return this->start <= rhs.start && this->end >= rhs.end;
}

bool Range::is_disjoint_from(const Range & rhs) const {
    return this->start < rhs.start && this->end < rhs.start;
}

bool Range::overlaps(const Range & rhs) const {
    return !this->is_disjoint_from(rhs) && !rhs.is_disjoint_from(*this);
}

std::string get_result(std::vector<Input> input) {
    std::string ret;
    uint count = 0;
    for (auto & ranges : input)
#if PART == 1
        count += ranges.r1.fully_contains(ranges.r2) || ranges.r2.fully_contains(ranges.r1);
#else
        count += ranges.r1.overlaps(ranges.r2);
#endif
    ret = std::to_string(count);
    return ret;
}
