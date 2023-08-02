// AOC - 2022 - 07
#include "answer.hpp"

#include <deque>
#include <fstream>
#include <iostream>
#include <sstream>

bool is_dir(std::string line) {
    return line.substr(0, 3) == "dir";
}

bool is_command(std::string line) {
    return line[0] == '$';
}

Dir* get_subdir(Dir* current_dir, const std::string& subdir_name) {
    for (auto& dir : current_dir->dirs)
        if (dir->name == subdir_name)
            return dir;

    std::cerr << "'" << subdir_name << "' not in " << current_dir->name
              << std::endl;
    error("couldn't find subdir");
}

Dir* handle_command(
    Dir* current_dir, std::string& cmd_line, std::ifstream& input) {
    std::cout << "CWD: " << current_dir->name << std::endl;
    std::cout << "Handling cmd: '" << cmd_line << "'" << std::endl;
    std::stringstream cmd_stream(cmd_line);
    std::string cmd, _;
    cmd_stream >> _; // $
    cmd_stream >> cmd;
    std::string line;

    Dir* reading_dir = current_dir;
    if (cmd == "ls") {
        if (!cmd_stream.eof()) {
            std::string dir_name;
            cmd_stream >> dir_name;
            reading_dir = get_subdir(current_dir, dir_name);
        }

        while (std::getline(input, line) && !is_command(line)) {
            if (is_dir(line)) {
                std::string dir_name = line.substr(4);
                std::cout << "Adding dir '" << dir_name << "' to "
                          << current_dir->name << std::endl;
                reading_dir->dirs.push_back(new Dir{reading_dir, dir_name});
            } else {
                uint size;
                std::string file_name;
                std::stringstream file_line_stream(line);
                file_line_stream >> size;
                file_line_stream >> file_name;
                reading_dir->files.push_back({size, file_name});
            }
        }
        std::cout << "After reading, the cwd looks like" << std::endl;
        std::cout << *reading_dir << std::endl;
        if (is_command(line))
            return handle_command(current_dir, line, input);
        else
            return current_dir;
    } else if (cmd == "cd") {
        std::string new_dirname;
        cmd_stream >> new_dirname;
        std::cout << "cd-ing to " << new_dirname << std::endl;
        if (new_dirname == "..") {
            std::cout << "\t thus to " << current_dir->parent->name
                      << std::endl;
            return current_dir->parent;
        } else
            return get_subdir(current_dir, new_dirname);
    } else {
        std::cerr << "Invalid cmd: " << cmd << std::endl;
        error("Invalid command");
    }
}

Input get_input(const char* filename) {
    std::ifstream stream(filename);
    std::string str;

    Dir* root = new Dir{nullptr, "/"};
    getline(stream, str); // cd /
    Dir* current_dir = root;

    while (getline(stream, str))
        current_dir = handle_command(current_dir, str, stream);

    std::cout << "current" << std::endl;
    std::cout << *current_dir << std::endl;
    std::cout << "root" << std::endl;
    std::cout << *root << std::endl;

    return {*root};
}

#define CUTOFF_SIZE 100000
#define FILESYSTEM_SIZE 70000000
#define NEEDED_SIZE 30000000

std::string get_result(Input input) {
    std::string ret;
#if PART == 1
    std::vector<Dir*> queue;
    queue.push_back(&input.root);
    int i = 0;
    uint res = 0;
    while (i < queue.size()) {
        std::cout << "ehhlo?" << std::endl;
        Dir d = *queue[i++];
        if (d.get_size() < CUTOFF_SIZE)
            res += d.get_size();
        for (auto& d : d.dirs)
            queue.push_back(d);
        for (auto& d : queue)
            std::cout << *d << std::endl;
    }
    ret = std::to_string(res);
#else
    uint space_to_free = input.root.get_size() - NEEDED_SIZE;
    std::cout << space_to_free << std::endl;
    std::vector<Dir*> queue;
    queue.push_back(&input.root);
    int i = 0;
    uint min_above_needed = -1;
    while (i < queue.size()) {
        Dir d = *queue[i++];
        if (d.get_size() < space_to_free)
            continue;
        else if (d.get_size() < min_above_needed)
            min_above_needed = d.get_size();

        for (auto& sub_dir : d.dirs)
            queue.push_back(sub_dir);
        for (auto& d : queue)
            std::cout << d->name << std::endl;
    }
    ret = std::to_string(min_above_needed);
#endif
    return ret;
}
