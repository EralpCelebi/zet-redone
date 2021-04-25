from sly import Lexer

class Syntax(Lexer):
    tokens = {
        "IDENTIFIER", "NUMBER",
        "FN",
    }

    NUMBER = r"[0-9]+"
    IDENTIFIER = r"[_\w][_\w0-9]*"
    
    IDENTIFIER["fn"] = "FN"

    literals = { '=', '+', '-', '*', '/', '(', ')', '{', '}', ';', '->' }

    ignore = r" \s+"
    ignore_comment = r'\#.*'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
