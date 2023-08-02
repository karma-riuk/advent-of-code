#include <deque>
#include <iostream>
#include <ostream>
#include <vector>

template <class T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& list) {
    unsigned long i = 0;
    os << "[";
    for (auto el : list) {
        os << el;
        if (i < list.size() - 1)
            os << ", ";
        i++;
    }
    os << "]";

    return os;
}

template <class T>
std::ostream& operator<<(std::ostream& os, const std::deque<T>& list) {
    unsigned long i = 0;
    os << "[";
    for (auto el : list) {
        os << el;
        if (i < list.size() - 1)
            os << ", ";
        i++;
    }
    os << "]";

    return os;
}

inline void error(const char* msg) {
    std::cerr << msg << std::endl;
    exit(1);
}
