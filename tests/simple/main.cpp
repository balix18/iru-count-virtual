#include <iostream>
#include <vector>
#include <memory>

class TAnimal {
public:
    virtual void Say() const {
        std::cout << "TAnimal.Say()" << std::endl;
    }
};

class Dog : public TAnimal {
public:
    virtual void Say() const {
        std::cout << "woof" << std::endl;
    }
};

class Cat : public TAnimal {
public:
    virtual void Say() const {
        std::cout << "meow" << std::endl;
    }
};

// Ez el van rontva, hiányzik a const
class Bird : public TAnimal {
public:
    virtual void Say() {
        std::cout << "tweet" << std::endl;
    }
};

class Mouse : public TAnimal {
public:
    virtual void Say() const {
        std::cout << "squeek" << std::endl;
    }
};

int main() {
    std::vector<std::unique_ptr<TAnimal>> animals{};

    animals.emplace_back(std::make_unique<Dog>());
    animals.emplace_back(std::make_unique<Cat>());
    animals.emplace_back(std::make_unique<Bird>());
    animals.emplace_back(std::make_unique<Mouse>());

    for (std::unique_ptr<TAnimal> const& animal : animals) {
        animal->Say();
    }
}
