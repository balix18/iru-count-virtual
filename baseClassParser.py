import regex as re

from functionSignature import FunctionSignature

# Cheat sheet
#
# \w : word characters (letter, digit, underscore)
# \s : whitespace characters
# \d : [0-9]
# . : bármilyen karakter

def debugPrint(pre, string):
    print(pre + " ->" + string + "<-")

def parseBaseVirtuals(contents, signatures):
    # print("-- parseBaseVirtuals --")

    # olyan class, ami senkinek sem a leszármazottja
    #
    # class-al kezdődik, 
    # legalább 1 whitespace
    # az osztály neve
    # legalább 1 whitespace
    # osztály definició elkezdése jel
    # bármennyi bármilyen karakter
    #      *? : de ne legyen greedy
    # virtual kilcsszó
    # legalább 1 whitespace
    # visszatérési típus
    # legalább 1 whitespace
    # a függvény neve
    # nyitó zárójel a paramétereknek
    # bármilyen karakterek a paramétereknek
    # lezáró zárójel a paramétereknek
    # legalább 1 whitespace
    # vagy van const kulcsszó vagy nincs
    # függvénydefinicíó elkezdése jel

    classHeader = r"class(?:\s+)([\w]+)(?:\s+){"
    anythingHeader = r"([\s\S]*?)"
    virtualHeader = r"(virtual)(?:\s+)([\w]+)(?:\s+)([\w]+)\((.*)\)(?:\s+)(\s?|const)(?:\s*)({)"
    pattern = re.compile(classHeader + anythingHeader + virtualHeader, re.MULTILINE)

    while True:
        match = pattern.search(contents)

        # ha egyáltalán semmi többet nem talál, akkor kész, nincs több
        if (match == None):
            # print("Nincs több illesztkedés")
            break

        # talált valamit, de még nem biztos hogy jót
        baseClassGroup    = match.group(1)     
        anythingGroup     = match.group(2)
        virtualGroup      = match.group(3)
        typeGroup         = match.group(4)
        nameGroup         = match.group(5)
        parameteresGroup  = match.group(6)
        isConstGroup      = match.group(7)
        funcDefSign       = match.group(8)

        # ha talált egy másik class-t a köztes részben, akkor az azt jelenti, hogy kimentünk a blokkunkból
        # tehát ez már nem jó, felül kellene írni a legelső class-t, hogy legközelebb ne találjuk meg
        if "class" in anythingGroup:
            startOfBaseClassGroup = match.start(1)
            endOfBaseClassGroup = match.end(1)
            contents = contents[ : startOfBaseClassGroup] + contents[endOfBaseClassGroup : ]
            continue

        startOfVirtualGroup = match.start(3)
        endOfFuncDefSign = match.end(8) - 1
        prettySignature = contents[startOfVirtualGroup : endOfFuncDefSign]

        isConstBool = isConstGroup == "const"

        # FG object
        fg = FunctionSignature(baseClassGroup, "AbstractBase", typeGroup, nameGroup, parameteresGroup, isConstBool, prettySignature)
        signatures.add(fg)

        # Signatúra eltávolítása
        contents = contents[ : startOfVirtualGroup] + contents[endOfFuncDefSign : ]

        # Debug print
        #print(contents)
    
    return contents
