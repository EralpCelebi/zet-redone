from sly import Lexer

class Syntax(Lexer):
    tokens = {"IDENTIFIER", "SEMICOLON"}
    
    IDENTIFIER = r"[_\w][_\w0-9]*"
    SEMICOLON =  r"\;"
    
    ignore = r" \s+"
    ignore_comment = r'\#.*'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
