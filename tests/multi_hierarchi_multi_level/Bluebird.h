#pragma once

#include "TBird.h"

class Bluebird : public TBird {
public:
    // El van rontva, hiányzik a const
    virtual void Say();

    // El van rontva, ott van pluszba a const
    virtual bool Fly(unsigned meter) const;
};
