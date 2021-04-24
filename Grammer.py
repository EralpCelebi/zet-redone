from sly import Parser
from Syntax import Syntax

from Nodes import Allocate, Group, Kind

class Grammer(Parser):
    tokens = Syntax.tokens

    @_("statements statement")
    def statements(self, p):
        return p.statements.Push(p.statement)

    @_("statement")
    def statements(self, p):
        return Group([p.statement])

    @_("allocate SEMICOLON")
    def statement(self, p):
        return p.allocate

    @_("kind IDENTIFIER")
    def allocate(self, p):
        return Allocate(p.kind, p.IDENTIFIER)

    @_("IDENTIFIER")
    def kind(self, p):
        return Kind(p.IDENTIFIER)
