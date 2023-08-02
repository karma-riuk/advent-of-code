#include <string>
#include "lib.hpp"

#ifndef VERBOSE
#define VERBOSE 0
#endif

#ifndef PART
#define PART 1
#endif

struct Range{
    uint start, end;
    bool operator ==(const Range & rhs) const{
        return this->start == rhs.start && this->end == rhs.end;
    }
    bool fully_contains(const Range & rhs) const;
    bool overlaps(const Range & rhs) const;
    bool is_disjoint_from(const Range & rhs) const;
};

struct Input{
    Range r1, r2;

    bool operator ==(const Input & rhs) const{
        return this->r1 == rhs.r1 && this->r2 == rhs.r2;
    }
};

inline std::ostream& operator<<(std::ostream &os, Range & range){
    os << "[" << range.start << ", " << range.end << "]";
    return os;
}

inline std::ostream& operator<<(std::ostream &os, Input & inp){
    os << inp.r1 << " & " << inp.r2;
    return os;
}


std::vector<Input> get_input(const char *);

std::string get_result(std::vector<Input>);


