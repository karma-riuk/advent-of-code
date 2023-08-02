#include "lib.hpp"

#include <string>

#ifndef VERBOSE
#define VERBOSE 0
#endif

#ifndef PART
#define PART 1
#endif

struct A {
    bool operator==(const A& rhs) const {
        return this->== rhs.;
    }
};

typedef A Input;

inline std::ostream& operator<<(std::ostream& os, Input& inp) {
    os << inp.;
    return os;
}

Input get_input(const char*);

std::string get_result(Input&);
