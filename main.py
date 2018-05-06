import os
import argparse
import projection_parser

def commandLineArgParser():
    parser = argparse.ArgumentParser(description='Count virtual')
    parser.add_argument('Directory', help='Könyvtár ahol a vizsgálatot el kell végezni')
    args = parser.parse_args()

    return args.Directory

def findHeaderFiles(listOfFiles):
    headerFiles = set()

    # print("Ezeket a C++ fájlokat találtam a könyvtárban:")
    for file in listOfFiles:
        # csak azok kellenek amiknek .cpp vagy .h a kiterjesztése
        if not file.lower().endswith(('.cpp', '.h')):
            listOfFiles.remove(file)
            continue
        
        if file.lower().endswith('.h'):
            headerFiles.add(file)
        
        # print(f"- {file}")

    return headerFiles

def main():

    # Debug, statikus könyvtár megadás
    workDirectory = ".\\tests\\multi_hierarchi_multi_level\\"

    # command line arg parser
    # workDirectory = commandLineArgParser()

    if not workDirectory.endswith('\\'):
        workDirectory = workDirectory + ' \\'

    # minden fájl és könyvtár a megadott könyvtárban
    listOfFiles = os.listdir(workDirectory)

    # csak a header file-ok
    headerFiles = findHeaderFiles(listOfFiles)

    print("Ezeket a C++ header fájlokat találtam a könyvtárban:")
    for headerFile in headerFiles:
        print(f"- {headerFile}")

    projection_parser.collectSignaturesFromHeaderFiles(workDirectory, headerFiles)


if __name__ == "__main__":
    main()
