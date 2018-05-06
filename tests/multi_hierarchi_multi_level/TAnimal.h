#pragma once

class TAnimal {
private:
    unsigned unifiedId;
    float mass;

public:
    TAnimal(unsigned unifiedId = 1000)
        : unifiedId{ unifiedId } { }

    virtual void Say() const;
};
