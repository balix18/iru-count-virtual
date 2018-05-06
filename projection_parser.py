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
        # print(base.ToString())

        # meg kell keresni azokat, akik belőle származnak le
        for signature in signatures:
            if signature.baseClass == base.derivedClass:
                # kényelmesebbb névre nevezése
                derived = signature

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


def testFunc(contents):
    signatures = set()

    # signatures kigyűjtése
    contents = baseClassParser.parseBaseVirtuals(contents, signatures)
    contents = derivedClassParser.parseDerivedVirtuals(contents, signatures)
    
    # a legfelső hierarchia kiválasztása
    bases = set()

    print("Begyűjtött szignatúra lista:")
    for signature in signatures:
        print(f" - {signature.ToString()}")
        # print(signature.IsDerived())
        # print(signature.ToPretty())

        # ki kell választani a Base-eket
        if signature.IsBase():
            bases.add(signature)

    print("\nEzeket találtam:")

    # el kell indítani a vizsgálatot
    recursionLookup(bases, signatures)
