#include <iostream>
#include <string>
#include "lib.hpp"

enum Move { 
    ROCK,
    PAPER,
    SCISSORS
};


struct Input{
    Move my, opponent;

    bool operator ==(const Input & rhs) const{
        return this->my == rhs.my && this->opponent == rhs.opponent;
    }
};

inline std::ostream& operator<<(std::ostream &os, Input & inp){
    os << "my: " << inp.my << ", opponent: " << inp.opponent;
    return os;
}


#ifndef VERBOSE
#define VERBOSE 0
#endif
std::vector<Input> get_input(const char *);

std::string get_result(std::vector<Input>);

inline void error(const char * msg){
    std::cerr << msg << std::endl;
    exit(1);
}
