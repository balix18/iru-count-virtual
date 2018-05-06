#pragma once

#include "TMammal.h"

class Mouse : public TMammal {
public:
    // El van rontva, hiányzik a const
    virtual void Say();
};
