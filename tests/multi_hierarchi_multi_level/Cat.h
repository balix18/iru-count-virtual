#pragma once

#include "TMammal.h"

class Cat : public TMammal {
public:
    // El van rontva, hiányzik a const
    virtual void Say();
};
