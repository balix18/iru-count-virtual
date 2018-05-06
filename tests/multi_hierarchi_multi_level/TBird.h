#pragma once

#include "TAnimal.h"

class TBird : public TAnimal {
public:
    static bool IsDead() {
        // sad
        return true;
    }

    // El van rontva, hiányzik a const
    virtual void Say();

    virtual bool Fly(unsigned meter);
};
