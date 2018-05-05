import baseClassParser
import derivedClassParser
from functionSignature import FunctionSignature

def testFunc(contents):
    signatures = set()

    contents = baseClassParser.parseBaseVirtuals(contents, signatures)
    contents = derivedClassParser.parseDerivedVirtuals(contents, signatures)
    
    for signature in signatures:
        print(signature.ToString())
        # print(signature.ToPretty())


# TODO Az öröklési hierarcha mélyebb lehet 1-nél (pl nem direkt öröklésnél)
