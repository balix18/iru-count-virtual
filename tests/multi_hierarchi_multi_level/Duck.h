#pragma once

#include "TBird.h"

class Duck : public TBird {
public:
    virtual void Say() const;

    virtual bool Fly(unsigned meter);
};
