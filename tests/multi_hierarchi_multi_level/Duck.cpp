#include "Duck.h"

#include <iostream>

void Duck::Say() const {
    std::cout << "quack" << std::endl;
}

bool Duck::Fly(unsigned meter) {
    std::cout << "i cant even fly" << std::endl;
    return false;
}
