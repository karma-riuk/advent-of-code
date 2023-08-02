#include "lib.hpp"

#include <cstdint>
#include <string>

#ifndef VERBOSE
#define VERBOSE 0
#endif

#ifndef PART
#define PART 2
#endif


typedef uint8_t Tree;

struct Forest {
    uint width, height;
    std::vector<Tree> trees;

    bool operator==(const Forest& rhs) const {
        return this->trees == rhs.trees;
    }

    uint get_idx(uint x, uint y) {
        return y * width + x;
    }

    Tree tree_at(uint x, uint y) {
        return trees[get_idx(x, y)];
    }
};

typedef Forest Input;

inline std::ostream& operator<<(std::ostream& os, Input& inp) {
    uint col = 0;
    for (auto& tree : inp.trees) {
        os << tree;
        if (++col % inp.width == 0)
            os << '\n';
    }
    return os;
}

Input get_input(const char*);

std::string get_result(Input&);
