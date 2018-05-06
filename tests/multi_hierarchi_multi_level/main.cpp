#include <iostream>
#include <vector>
#include <memory>

#include "TAnimal.h"
#include "Dog.h"
#include "Cat.h"
#include "Mouse.h"
#include "Bluebird.h"
#include "Duck.h"
#include "Frog.h"

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
