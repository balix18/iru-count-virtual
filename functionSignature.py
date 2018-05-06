class FunctionSignature(object):

    def __init__(self, derivedClass, baseClass, type, name, parameteres, isConst, pretty):
        self.derivedClass = derivedClass
        self.baseClass = baseClass
        self.type = type
        self.name = name
        self.parameteres = parameteres
        self.isConst = isConst
        self.pretty = pretty

    def IsBase(self):
        return self.baseClass == "AbstractBase"

    def IsDerived(self):
        return not self.IsBase()

    # Itt nem kell vizsgálni, hogy a const egyezik-e
    def IsTheSignatureSubStructureSame(self, base):
        return self.type == base.type and \
            self.name == base.name and \
            self.parameteres == base.parameteres

    def IsVirtualOverrideCorrect(self, base):
        if self.baseClass != base.derivedClass:
            raise RuntimeError("Nem jó a leszármazási kapcsolat")

        return self.IsTheSignatureSubStructureSame(base) and \
            self.isConst == base.isConst

    def GetFunctionDefinitionString(self):
        const = f" const" if self.isConst else f""
        return f"{self.type} {self.name}({self.parameteres}){const}"

    def ToString(self):
        unifiedClass = f"{self.derivedClass}" if self.IsBase() else f"{self.derivedClass}:{self.baseClass}"
        return f"{unifiedClass} {self.GetFunctionDefinitionString()}"

    def ToPretty(self):
        return f"{self.pretty}"
