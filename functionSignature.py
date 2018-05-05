class FunctionSignature(object):

    def __init__(self, derivedClass, baseClass, type, name, parameteres, isConst, pretty):
        self.derivedClass = derivedClass
        self.baseClass = baseClass
        self.type = type
        self.name = name
        self.parameteres = parameteres
        self.isConst = isConst
        self.pretty = pretty

    def ToString(self):
        unifiedClass = f"{self.baseClass}" if self.derivedClass == "Nothing" else f"{self.derivedClass}:{self.baseClass}"
        return f"{unifiedClass} {self.type} {self.name} ({self.parameteres}) {self.isConst}"

    def ToPretty(self):
        return f"{self.pretty}"
