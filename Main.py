from os import system
from os.path import splitext
from sys import argv

from colorama import init, Fore, Back, Style

from Syntax import Syntax
from Grammer import Grammer
from Passport import Passport

import llvmlite.binding as llvm

syntax: Syntax = Syntax()
grammer: Grammer = Grammer()

llvm.initialize()
llvm.initialize_all_targets()
llvm.initialize_native_asmprinter()

init()

data = ""

with open(argv[1], "r") as f:
    data = f.read()

out = grammer.parse(syntax.tokenize(data))

state = Passport()

out.Build(state)

print(Fore.RED + Style.BRIGHT + "==================== IR ====================" + Fore.RESET)

print(state.module)

print(Fore.RED + Style.BRIGHT + "============================================" + Fore.RESET)

with open(splitext(argv[1])[0]+".ll", "w") as f:
    f.write(str(state.module))