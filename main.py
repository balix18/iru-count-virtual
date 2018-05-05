import projection_parser 

def main():
    f = open("tests/simple/main.cpp", "r")

    contents = f.read()

    projection_parser.testFunc(contents)

if __name__ == "__main__":
    main()
