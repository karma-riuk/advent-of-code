// AOC - 2022 - 01
#include "answer.hpp"
#include <cstdlib>
#include <iostream>
#include <fstream>

std::vector<Input> get_input(const char * filename){
    std::ifstream stream(filename);
    std::string str;
    std::vector<Input> ret;
    ret.push_back(*new Input());

    while (getline(stream, str)){
        if (str.length() == 0) 
            ret.push_back(*new Input());
        else 
            ret.back().calories.push_back(stoi(str));
    }
    return ret;
}

std::string get_result(std::vector<Input> inputs){
    std::string ret;
#if PART==1
    uint max_sum = 0;
    for (auto& inp: inputs){

        uint local_sum = 0;
        for (auto& n : inp.calories)
            local_sum += n;
        std::cout << local_sum << std::endl;
        if (local_sum > max_sum)
            max_sum = local_sum;
    }
    ret = std::to_string(max_sum);
    std::cout << ret << std::endl;
#else
    std::vector<uint> top3(3);
    for (int i = 0; i < 3; i++){
        uint max_sum = 0;
        size_t max_idx = -1;
        size_t idx = 0;
        for (auto& inp: inputs){

            uint local_sum = 0;
            for (auto& n : inp.calories)
                local_sum += n;
            std::cout << local_sum << std::endl;
            if (local_sum > max_sum) {
                max_sum = local_sum;
                max_idx = idx;
            }
            idx++;
        }
        top3.push_back(max_sum);
        inputs.erase(inputs.begin() + max_idx);
    }

    uint sum = 0;
    for (auto& n : top3)
        sum += n;
    ret = std::to_string(sum);

    std::cout << ret << std::endl;
#endif
    return ret;

}
