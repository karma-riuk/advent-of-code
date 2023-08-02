// AOC - 2022 - 02
#include "answer.hpp"
#include <iostream>
#include <fstream>

Move get_move(const char & move){
    if (move == 'A' || move == 'X')
        return Move::ROCK;
    if (move == 'B' || move == 'Y')
        return Move::PAPER;
    if (move == 'C' || move == 'Z')
        return Move::SCISSORS;
    error("Move not valid");
}


std::vector<Input> get_input(const char * filename){
    std::ifstream stream(filename);
    std::string str;
    std::vector<Input> ret;

    while (getline(stream, str)){
#if PART == 1
        ret.push_back({
                .my = get_move(str[2]),
                .opponent = get_move(str[0])
                });
#else
        Move opponent = get_move(str[0]);
        Move my;
        switch (str[2]) {
            case 'X': // lose
                my = static_cast<Move>((opponent - 1 + 3) % 3);
                break;
            case 'Y': // draw
                my = opponent;
                break;
            case 'Z': // win
                my = static_cast<Move>((opponent + 1) % 3);
                break;
            default:
                error("Part 2 move not valid");
        }
        ret.push_back({
                .my = my,
                .opponent = opponent
                });
#endif
    }
    return ret;
}

std::string get_result(std::vector<Input> input){
    std::string ret;
    uint score = 0;

    for (auto round : input){
        std::cout << "before: " << score << std::endl;
        score += round.my + 1;
        if (round.my == round.opponent){ // draw
            score += 3;
            continue;
        }
        std::cout << round.my << " " << round.opponent << std::endl;
        if (round.my == (round.opponent + 1) % 3){ // win
            std::cout << "win" << std::endl;
            score += 6;
        } 
        std::cout << "after: " << score << std::endl;
    }
    ret = std::to_string(score);

    return ret;
}
