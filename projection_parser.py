import baseClassParser
import derivedClassParser
from functionSignature import FunctionSignature

# TODO Az öröklési hierarcha mélyebb lehet 1-nél (pl nem direkt öröklésnél)
# a parser-nek működnie kellene ilyen esetben is, viszont a keresésnél már rekurzió kellene

def testFunc(contents):
    signatures = set()

    contents = baseClassParser.parseBaseVirtuals(contents, signatures)
    contents = derivedClassParser.parseDerivedVirtuals(contents, signatures)
    
    bases = set()
    print("Signature list: ")
    for signature in signatures:
        print(f" - {signature.ToString()}")
        # print(signature.IsDerived())
        # print(signature.ToPretty())

        # ki kell választani a Base-eket
        if signature.IsBase():
            bases.add(signature)

    print("\nKeresem...")
    for base in bases:
        # print(base.ToString())

        # meg kell keresni azokat, akik belőle származnak le
        for signature in signatures:
            if signature.baseClass == base.derivedClass:
                derived = signature
                # print(derived.derivedClass)

                # meg kell nézni a const-ot
                if not derived.IsVirtualOverrideCorrect(base):
                    print(f"Hibás használat a(z) {derived.derivedClass} osztályban!" )
                    print(f"\t\'{derived.GetFunctionDefinitionString()}\' helyett")
                    print(f"\t\'{base.GetFunctionDefinitionString()}\' kellene.")
