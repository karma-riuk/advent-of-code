#include "lib.hpp"

#include <string>

#ifndef VERBOSE
#define VERBOSE 0
#endif

#ifndef PART
#define PART 2
#endif

struct File {
    uint size;
    std::string name;

    bool operator==(const File& rhs) const {
        return this->name == rhs.name && this->size == rhs.size;
    }
};

struct Dir {
    Dir* parent;
    std::string name;
    std::vector<Dir*> dirs;
    std::vector<File> files;
    uint size = 0;

    uint get_size() {
        if (this->size > 0)
            return this->size;
        uint res = 0;
        for (auto& f : this->files)
            res += f.size;

        for (auto& d : this->dirs)
            res += d->get_size();
        this->size = res;
        return res;
    }

    bool operator==(const Dir& rhs) const {
        return this->name == rhs.name && this->dirs == rhs.dirs &&
               this->files == rhs.files;
    }
};

struct Input {
    Dir root;

    bool operator==(const Input& rhs) const {
        return this->root == rhs.root;
    }
};

inline std::ostream& operator<<(std::ostream& os, File& file) {
    os << "- " << file.name << " (file, size=" << file.size << ")" << std::endl;
    return os;
}

inline std::ostream& operator<<(std::ostream& os, Dir& dir) {
    os << "- " << dir.name << " (dir";
    if (dir.parent)
        os << ", parent=" << dir.parent->name;
    os << ")" << std::endl;
    for (auto& d : dir.dirs)
        os << '\t' << *d;
    for (auto& f : dir.files)
        os << '\t' << f;
    return os;
}

inline std::ostream& operator<<(std::ostream& os, Input& inp) {
    os << inp.root;
    return os;
}

Input get_input(const char*);

std::string get_result(Input);
