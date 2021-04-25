import llvmlite.binding as llvm
from llvmlite import ir

from Passport import Passport
from Data import Data

from Access import Target, Source

class Group:
    def __init__(self, elements: list):
        self.elements = elements
    
    def Push(self, value):
        self.elements.append(value)
        return self

    def Pop(self):
        return self.elements.pop
    
    def Build(self, passport: Passport):
        for element in self.elements:
            element.Build(passport)

class Assign:
    def __init__(self, target, source):
        self.target = target
        self.source = source
    
    def Build(self, passport: Passport):
        passport.Set("isTarget")
        self.target.Build(passport)
        passport.Unset("isTarget")

        passport.Set("isSource")
        self.source.Build(passport)
        passport.Unset("isSource")

        passport.builder.store(
            Source(passport, passport.flags["source"]),
            Target(passport, passport.flags["target"])
        )

class Allocate:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name
    
    def Build(self, passport: Passport):
        self.kind.Build(passport)

        passport.variables[self.name] = Data({
            "kind": passport.flags["kind"],
            "llvm": passport.flags["kind"].Get("llvm"),
            "source": "Load",
            "target": "Direct",
            "value": passport.builder.alloca(
                passport.flags["kind"].Get("llvm"),
                name=self.name
            )
        })

        passport.flags["needed"] = passport.flags["kind"]
        passport.flags["target"] = passport.variables[self.name]

class Variable:
    def __init__(self, name):
        self.name = name

    def Build(self, passport: Passport):
        if passport.Get("isTarget"):
            passport.flags["needed"] = passport.variables[self.name].Get("kind")
            passport.flags["target"] = passport.variables[self.name]
        
        elif passport.Get("isSource"):
            passport.flags["source"] = passport.variables[self.name]

        else:
            passport.flags["value"] = passport.variables[self.name]

class Integer:
    def __init__(self, value):
        self.value = int(value)
    
    def Build(self, passport: Passport):
        needed = Data({
            "name": "i32",
            "llvm": ir.IntType(32),
            "depth": 0
        })

        if passport.Get("needed"):
            needed = passport.Get("needed")
        
        passport.flags["source"] = Data({
            "kind": needed,
            "llvm": needed.Get("llvm"),
            "source": "Load",
            "target": "Direct",
            "value": passport.builder.alloca(needed.Get("llvm"))
        })

class Kind:
    def __init__(self, kind):
        self.kind = kind

    def Build(self, passport: Passport):
        passport.flags["kind"] = Data({
            "name": self.kind,
            "llvm": passport.types[self.kind],
            "depth": 0
        }) 