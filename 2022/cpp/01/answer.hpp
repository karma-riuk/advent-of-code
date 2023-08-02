#include <string>
#include <vector>
#include <ostream>

template<class T>
std::ostream &operator<<(std::ostream &os, const std::vector<T> &list) {
    unsigned long i = 0;
    os << "[";
    for (auto el : list) {
        os << el;
        if (i < list.size() - 1) {
            os << ", ";
        }
        i++;
    }
    os << "]";

    return os;
}

struct Input{
    std::vector<uint> calories;

    bool operator ==(const Input & rhs) const{
        return this->calories == rhs.calories;
    };
};

inline std::ostream& operator<<(std::ostream &os, Input & inp){
    os << inp.calories;
    return os;
}


#ifndef VERBOSE
#define VERBOSE 0
#endif
std::vector<Input> get_input(const char *);

std::string get_result(std::vector<Input>);

