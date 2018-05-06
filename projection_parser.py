import baseClassParser
import derivedClassParser
from functionSignature import FunctionSignature

def lookupVirtualFunctionInWholeBaseClass(signatures, derived, base):
    # megnézi hogy a potenciális base-eknek létezik-e olyan fv-e, ami a derived-ben benne van
    # ha létezik, az azt jelenti, hogy nem friss ágon jött be a virtuális függvény, már előtte is
    # ott volt a base osztályban
    for signature in signatures:
        # ha ugyanaz az osztály, de a fv lehet más
        if signature.IsTheSameClass(base):
            # ha ugyanaz lényegében a fv is
            if derived.IsTheSignatureSubStructureSame(signature):
                return True

    # ha átnéztünk mindent, de nincs ilyen, teljesen új fv-ről van szó
    return False


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
                # kényelmesebbb névre nevezése, most hogy már tudjuk hogy leszármazott
                derived = signature

                # meg kell nézni, hogy új ágon (frissen) nem jön-e be újabb virtuális függvény,
                # ha false, akkor új virtuális fv van a derivedben
                if lookupVirtualFunctionInWholeBaseClass(signatures, derived, base) == False:
                    # mivel nincs ilyen, így onnan mint base, elkezdhetjük felgöngyölíteni a szálat
                    newBases.add(derived)
                    continue

                # ha jó a leszármazási hierarchia, de teljesen más fv-ről van szó, akkor azt nem
                # kell tovább vizsgálni
                if not derived.IsTheSignatureSubStructureSame(base):
                    continue

                # következő szinten őt is vizsgálni kell majd, mint base
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
