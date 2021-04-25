import llvmlite.binding as llvm
import llvmlite.ir as ir

class Passport:
    def __init__(self):
        self.module = ir.Module("zet")

        fntype = ir.FunctionType(ir.IntType(8), [])
        fn = ir.Function(self.module, fntype, 'main')

        self.block: ir.Block = fn.append_basic_block()
        self.builder: ir.IRBuilder = ir.IRBuilder(self.block)

        self.flags = {}

        self.variables = {}
        self.functions = {}

        self.types = {"i8": ir.IntType(8)}
        self.structs   = {}

    def Get(self, target):
        try:
            return self.flags[target]
        except:
            return False

    def Set(self, target) -> bool:
        try:
            self.flags[target] = True
            return True
        except:
            return False
        
    def Unset(self, target) -> bool:
        try:
            self.flags[target] = False
            return True
        except:
            return False