#include "TBird.h"

#include <iostream>

void TBird::Say() {
    std::cout << "TBird.Say()" << std::endl;
}

bool TBird::Fly(unsigned meter) {
    std::cout << "TBird.Fly(meter)" << std::endl;
    return true;
}
