from sly import Parser

from Nodes import Allocate, Assign, Group, Integer, Kind, Variable
from Syntax import Syntax


class Grammer(Parser):
    tokens = Syntax.tokens

    @_('FN IDENTIFIER "(" ")" "->" kind "{" "}"')
    def function(self, p):
        pass
    
    @_('statements statement')
    def statements(self, p):
        return p.statements.Push(p.statement)

    @_('statement')
    def statements(self, p):
        return Group([p.statement])

    @_('assign ";"')
    @_('allocate ";"')
    def statement(self, p):
        return p[0]

    @_('target "=" source')
    def assign(self, p):
        return Assign(p.target, p.source)

    @_('allocate')
    @_('variable')
    def target(self, p):
        return p[0]

    @_('expression')
    def source(self, p):
        return p[0]

    @_('number')
    @_('variable')
    def expression(self, p):
        return p[0]

    @_('kind IDENTIFIER')
    def allocate(self, p):
        return Allocate(p.kind, p.IDENTIFIER)

    @_('IDENTIFIER')
    def variable(self, p):
        return Variable(p.IDENTIFIER)

    @_('NUMBER')
    def number(self, p):
        return Integer(p.NUMBER)

    @_('IDENTIFIER')
    def kind(self, p):
        return Kind(p.IDENTIFIER)
