#include "lib.hpp"

#include <sstream>
#include <string>

#ifndef VERBOSE
#define VERBOSE 0
#endif

#ifndef PART
#define PART 2
#endif

struct Input {
    std::string str;

    bool operator==(const Input& rhs) const {
        return this->str == rhs.str;
    }
};

inline std::ostream& operator<<(std::ostream& os, Input& inp) {
    os << inp.str;
    return os;
}

Input get_input(const char*);

std::string get_result(Input);
