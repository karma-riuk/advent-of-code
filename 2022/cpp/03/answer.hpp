#include <iostream>
#include <string>
#include "lib.hpp"

#ifndef PART
#define PART 2
#endif

#ifndef VERBOSE
#define VERBOSE 0
#endif

struct Input{
    std::string content;
    bool operator ==(const Input & rhs) const{
        return this->content == rhs.content;
    }
};

inline std::ostream& operator<<(std::ostream &os, Input & inp){
    os << inp.content;
    return os;
}

std::vector<Input> get_input(const char *);

std::string get_result(std::vector<Input>);

inline void error(const char * msg){
    std::cerr << msg << std::endl;
    exit(1);
}

