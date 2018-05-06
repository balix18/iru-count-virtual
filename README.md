# Count Virtual

## Feladatazonosító:

    S2018-13

## Feladat leírása:

Egy paraméterként megadott könyvtárban található és a C++ szabvány szerint hiba nélkül forduló több fájlból álló modern C++ kódban keresse meg azokat a virtuális tagfüggvényeket, amelyek a leszármaztatott osztályokban potenciálisan rosszul lettek felüldefiniálva, azaz a tagfüggvény maga egy const típusmódosítóban különbözik a felüldefiniált, felüldefiniálni vágyott virtuális tagfüggvénytől.

## Követelmények a futtatáshoz

- Python 3.6+

Csak ennyi, semmilyen extra modult nem használ, amit még pluszba le kellene tölteni.

## Indítási argumentum

Ha paraméter nélkül kerül elindításra, akkor kiírja hogy, szeretne egy könyvtár útvonalát megkapni, amiben a vizsgálatot elvégezheti

~~~bash
$ python .\main.py

usage: main.py [-h] Directory
main.py: error: the following arguments are required: Directory
~~~

A `--help` már használhatóbb információt is ad, hogy mi hiányzik neki

~~~bash
$ python .\main.py --help

usage: main.py [-h] Directory

Count virtual

positional arguments:
  Directory   Könyvtár ahol a vizsgálatot el kell végezni

optional arguments:
  -h, --help  show this help message and exit
~~~

## Példa a program futására

A következő példában a `.\tests\multi_hierarchi_multi_level\` könyvtárban fogja vizsgálni a forráskódot.

~~~cpp
$ python .\main.py .\tests\multi_hierarchi_multi_level\
Ezeket a C++ header fájlokat találtam a könyvtárban:
- Frog.h
- Mouse.h
- TAnimal.h
- Dog.h
- TBird.h
- Bluebird.h
- Cat.h
- TMammal.h
- Duck.h

Begyűjtött virtuális szignatúra lista:
 - Bluebird:TBird void Say();
 - TAnimal void Say() const;
 - Bluebird:TBird bool Fly(unsigned meter) const;
 - Dog:TMammal void Say() const;
 - Cat:TMammal void Say();
 - Duck:TBird void Say() const;
 - TMammal:TAnimal void Say() const;
 - Frog:TAnimal void Say() const;
 - Duck:TBird bool Fly(unsigned meter);
 - Mouse:TMammal void Say();
 - TBird:TAnimal void Say();
 - TBird:TAnimal bool Fly(unsigned meter);

Ezeket a hibákat találtam:
Hibás használat a(z) TBird osztályban!
        'void Say();' helyett
        'void Say() const;' kellene.

Hibás használat a(z) Bluebird osztályban!
        'bool Fly(unsigned meter) const;' helyett
        'bool Fly(unsigned meter);' kellene.

Hibás használat a(z) Cat osztályban!
        'void Say();' helyett
        'void Say() const;' kellene.

Hibás használat a(z) Mouse osztályban!
        'void Say();' helyett
        'void Say() const;' kellene.

Hibás használat a(z) Bluebird osztályban!
        'void Say();' helyett
        'void Say() const;' kellene.

~~~
