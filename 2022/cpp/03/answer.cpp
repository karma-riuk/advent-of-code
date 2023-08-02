// AOC - 2022 - 03
#include "answer.hpp"

#include <algorithm>
#include <cctype>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_set>

std::vector<Input> get_input(const char *filename) {
  std::ifstream stream(filename);
  std::string str;
  std::vector<Input> ret;

  while (getline(stream, str))
    ret.push_back({.content = str});
  return ret;
}

int get_priority(const char &c) {
  return std::islower(c) ? 1 + (c - 'a') : 27 + (c - 'A');
}

std::string get_result(std::vector<Input> input) {
  std::string ret;

  int score = 0;
#if PART == 1
  // filter through the first half to find common elements
  for (auto &sacks : input) {
    size_t size = sacks.content.size();
    if (size % 2 == 1)
      error("sack does not have even number of elements");

    std::string sack1 = sacks.content.substr(0, size / 2);
    std::string sack2 = sacks.content.substr(size / 2);
    std::unordered_set<char> common_items;

    std::copy_if(
        sack1.begin(), sack1.end(),
        std::inserter(common_items, common_items.end()),
        [sack2](char c) { return sack2.find(c) != std::string::npos; });

    std::cout << sacks << std::endl;
    std::cout << common_items << std::endl;

    // get priority of items found
    for (auto &item : common_items)
      score += get_priority(item);
    std::cout << "score: " << score << std::endl;
  }
#else
  std::vector<std::vector<std::string>> groups;
  for (size_t i = 0; i < input.size(); i += 3) {
    groups.insert(groups.end(), {input[i + 0].content, input[i + 1].content,
                                 input[i + 2].content});
  }
  for (auto &group : groups) {
    std::cout << group << std::endl;
    std::unordered_set<char> common_items;
    std::copy_if(group[0].begin(), group[0].end(),
                 std::inserter(common_items, common_items.end()),
                 [group](char c) {
                   return group[1].find(c) != std::string::npos &&
                          group[2].find(c) != std::string::npos;
                 });

    // get priority of items found
    for (auto &item : common_items)
      score += get_priority(item);
    std::cout << "score: " << score << std::endl;
  }
#endif
  ret = std::to_string(score);
  return ret;
}
