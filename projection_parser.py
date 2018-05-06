import baseClassParser
import derivedClassParser
from functionSignature import FunctionSignature

def recursionLookup(bases, signatures):
    # megállási feltétel, ha már nincs mit vizsgálni
    if len(bases) == 0:
        return

    # a következő szint osztályai
    newBases = set()

    # minden alapra megvizsgáljuk
    for base in bases:
        #print(base.ToString())

        # meg kell keresni azokat, akik belőle származnak le
        for signature in signatures:
            if signature.baseClass == base.derivedClass:
                # kényelmesebbb névre nevezése
                derived = signature

                if not derived.IsTheSignatureSubStructureSame(base):
                    continue

                # következő szinten őt is vizsgálni kell
                newBases.add(derived)

                # print(derived.derivedClass)

                # meg kell nézni hogy helyes-e az override
                if not derived.IsVirtualOverrideCorrect(base):
                    print(f"Hibás használat a(z) {derived.derivedClass} osztályban!" )
                    print(f"\t\'{derived.GetFunctionDefinitionString()}\' helyett")
                    print(f"\t\'{base.GetFunctionDefinitionString()}\' kellene.\n")

                    # a további vizsgálat érdekében ki kell javítani, hogy a mélyebb szinteken is vizsgálni lehessen
                    derived.isConst = base.isConst

    # tovább kell vizsgálódani az öröklési hierarchiában
    recursionLookup(newBases, signatures)


def examineVirtualFunctions(signatures):
    # a legfelső szintű hierarchia kiválasztása
    bases = set()

    # ki kell választani a Base-eket
    for signature in signatures:
        if signature.IsBase():
            bases.add(signature)

    # el kell indítani a vizsgálatot
    print("\nEzeket a hibákat találtam:")
    recursionLookup(bases, signatures)


def parseBaseAndDerivedSignatures(contents, signatures):
    contents = baseClassParser.parseBaseVirtuals(contents, signatures)
    contents = derivedClassParser.parseDerivedVirtuals(contents, signatures)


def collectSignaturesFromHeaderFiles(workDirectory, headerFiles):
    signatures = set()

    for headerFile in headerFiles:
        # print(workDirectory + headerFile)
        f = open(workDirectory + headerFile, "r")
        contents = f.read()

        parseBaseAndDerivedSignatures(contents, signatures)

    print("\nBegyűjtött virtuális szignatúra lista:")
    for signature in signatures:
        print(f" - {signature.ToString()}")
        # print(signature.IsDerived())
        # print(signature.ToPretty())

    examineVirtualFunctions(signatures)
