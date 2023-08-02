#include <stack>
#include <string>
#include "lib.hpp"

#ifndef VERBOSE
#define VERBOSE 0
#endif

#ifndef PART
#define PART 2
#endif

struct Move{
    uint item, from, to;

    bool operator ==(const Move & rhs) const{
        return this->item == rhs.item && this->from == rhs.from && this->to == rhs.to;
    }
};

typedef std::vector<std::vector<char>> stacks_t;

struct Input{
    stacks_t stacks;
    std::vector<Move> moves;
    bool operator ==(const Input & rhs) const{
        return this->moves == rhs.moves && this->stacks == rhs.stacks;
    }
};

inline std::ostream& operator<<(std::ostream &os, stacks_t & stacks){
    uint i = 0;
    for (auto & stack: stacks){
        os << i++ << " ";
        for (auto & item : stack)
            os << item << " ";
        os << std::endl;
    }
    return os;
}

inline std::ostream& operator<<(std::ostream &os, Move & move){
    os << "move " << move.item << " from " << move.from << " to " << move.to;
    return os;
}

inline std::ostream& operator<<(std::ostream &os, Input & inp){
    os << "---------------------------------" << std::endl;
    os << inp.stacks << std::endl;
    for (auto & move: inp.moves)
        os << move << std::endl;
    os << "---------------------------------" << std::endl;
    return os;
}


Input get_input(const char *);

std::string get_result(Input);


