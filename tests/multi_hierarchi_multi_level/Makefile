BINARY = a.out
OBJECTS = TAnimal.o TMammal.o TBird.o Dog.o Cat.o Mouse.o Bluebird.o Duck.o Frog.o main.o
HEADERS = TAnimal.h TMammal.h TBird.h Dog.h Cat.h Mouse.h Bluebird.h Duck.h Frog.h

CXX = g++-6

CXXFLAGS = -std=c++17 -O0 -Wall -Wdeprecated -pedantic -g

LDFLAGS = -g

.PHONY: all clean

all: $(BINARY)

clean:
	rm -f $(BINARY) $(OBJECTS)

$(BINARY): $(OBJECTS)
	$(CXX) $(LDFLAGS) $^ -o $@

%.o: %.c $(HEADERS)
	$(CC) $(CFLAGS) -c $< -o $@

%.o: %.cpp $(HEADERS)
	$(CXX) $(CXXFLAGS) -c $< -o $@
