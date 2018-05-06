#include <iostream>
#include <vector>
#include <memory>

class TAnimal {
private:
    float mass;

public:
    virtual void Say() const {
        std::cout << "TAnimal.Say()" << std::endl;
    }
};

class TMammal : public TAnimal {
public:
    virtual void Say() const {
        std::cout << "TMammal.Say()" << std::endl;
    }
};

// El van rontva, hiányzik a const
class TBird : public TAnimal {
public:
    virtual void Say() {
        std::cout << "TBird.Say()" << std::endl;
    }
};

class Dog : public TMammal {
public:
    virtual void Say() const {
        std::cout << "woof" << std::endl;
    }
};

// El van rontva, hiányzik a const
class Cat : public TMammal {
public:
    virtual void Say() {
        std::cout << "meow" << std::endl;
    }
};

// Ez el van rontva, hiányzik a const
class Mouse : public TMammal {
public:
    virtual void Say() {
        std::cout << "squeek" << std::endl;
    }
};

// Ez el van rontva, hiányzik a const
class Bluebird : public TBird {
public:
    virtual void Say() {
        std::cout << "tweet" << std::endl;
    }
};

class Duck : public TBird {
public:
    virtual void Say() const {
        std::cout << "quack" << std::endl;
    }
};

class Frog : public TAnimal {
public:
    virtual void Say() const {
        std::cout << "croak" << std::endl;
    }
};

int main() {
    std::vector<std::unique_ptr<TAnimal>> animals{};

    animals.emplace_back(std::make_unique<Dog>());
    animals.emplace_back(std::make_unique<Cat>());
    animals.emplace_back(std::make_unique<Mouse>());
    animals.emplace_back(std::make_unique<Bluebird>());
    animals.emplace_back(std::make_unique<Duck>());
    animals.emplace_back(std::make_unique<Frog>());
    

    for (std::unique_ptr<TAnimal> const& animal : animals) {
        animal->Say();
    }
}
