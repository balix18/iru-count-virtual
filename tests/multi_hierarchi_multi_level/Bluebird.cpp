#include "Bluebird.h"

#include <iostream>

void Bluebird::Say() {
    std::cout << "tweet" << std::endl;
}

bool Bluebird::Fly(unsigned meter) const {
    std::cout << "im on " << meter << "." << std::endl;
    return true;
}
