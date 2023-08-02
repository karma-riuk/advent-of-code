#include <ostream>
#include <vector>

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
