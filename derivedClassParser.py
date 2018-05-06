import regex as re

from functionSignature import FunctionSignature

def debugPrint(pre, string):
    print(pre + " ->" + string + "<-")

# Többszörös öröklésre nem működik, csak a direkt öröklése
def parseDerivedVirtuals(contents, signatures):
    # print("-- parseDerivedVirtuals --")

    derivedHeader = r"class(?:\s+)([\w]+)(?:\s+)\:(?:\s+)(?:public|private|protected)(?:\s+)([\w]+)(?:\s+){"
    anythingHeader = r"([\s\S]*?)"
    virtualHeader = r"(virtual)(?:\s+)([\w]+)(?:\s+)([\w]+)\((.*)\)(?:\s+)(\s?|const)(?:\s*)({)"
    pattern = re.compile(derivedHeader + anythingHeader + virtualHeader, re.MULTILINE)

    while True:
        match = pattern.search(contents)

        # ha egyáltalán semmi többet nem talál, akkor kész, nincs több
        if (match == None):
            # print("Nincs több illesztkedés")
            break

        # talált valamit, de még nem biztos hogy jót
        derivedClassGroup = match.group(1)
        baseClassGroup    = match.group(2)        
        anythingGroup     = match.group(3)
        virtualGroup      = match.group(4)
        typeGroup         = match.group(5)
        nameGroup         = match.group(6)
        parameteresGroup  = match.group(7)
        isConstGroup      = match.group(8)
        funcDefSign       = match.group(9)

        # ha talált egy másik class-t a köztes részben, akkor az azt jelenti, hogy kimentünk a blokkunkból
        # tehát ez már nem jó, felül kellene írni a legelső class-t, hogy legközelebb ne találjuk meg
        if "class" in anythingGroup:
            startOfBaseClassGroup = match.start(1)
            endOfBaseClassGroup = match.end(1)
            contents = contents[ : startOfBaseClassGroup] + contents[endOfBaseClassGroup : ]
            continue

        # Signatúra
        startOfVirtualGroup = match.start(4)
        endOfFuncDefSign = match.end(9) - 1
        prettySignature = contents[startOfVirtualGroup : endOfFuncDefSign]

        isConstBool = isConstGroup == "const"

        # FG object
        fg = FunctionSignature(derivedClassGroup, baseClassGroup, typeGroup, nameGroup, parameteresGroup, isConstBool, prettySignature)
        signatures.add(fg)

        # Signatúra eltávolítása
        contents = contents[ : startOfVirtualGroup] + contents[endOfFuncDefSign : ]

        # Debug print
        #print(contents)
        
    return contents
