from enum import Enum, auto
from dataclasses import dataclass
from typing import Any

class TokenType(Enum):
    # Single-character tokens
    LPAREN = auto(); RPAREN = auto(); LBRACE = auto(); RBRACE = auto()
    LBRACKET = auto(); RBRACKET = auto(); COMMA = auto(); DOT = auto()
    MINUS = auto(); PLUS = auto(); SEMICOLON = auto(); SLASH = auto()
    STAR = auto(); PERCENT = auto()

    # One or two character tokens
    BANG = auto(); BANGEQ = auto()
    EQ = auto(); EQEQ = auto()
    GT = auto(); GTEQ = auto()
    LT = auto(); LTEQ = auto()

    # Literals
    IDENTIFIER = auto(); STRING = auto(); NUMBER = auto()

    # Keywords
    AND = auto(); OR = auto(); IF = auto(); ELSE = auto()
    FALSE = auto(); TRUE = auto(); FN = auto(); LET = auto()
    NULL = auto(); RETURN = auto(); WHILE = auto()
    BREAK = auto(); CONTINUE = auto(); PRINT = auto()
    NOT = auto()

    EOF = auto()

@dataclass
class Token:
    type: TokenType
    value: Any
    line: int

    def __repr__(self):
        return f"Token({self.type.name}, {repr(self.value)}, {self.line})"

class LexError(Exception):
    def __init__(self, line: int, message: str):
        self.line = line
        self.message = message
        super().__init__(f"[LexError line {line}] {message}")

class Lexer:
    KEYWORDS = {
        "and": TokenType.AND, "or": TokenType.OR, "if": TokenType.IF,
        "else": TokenType.ELSE, "false": TokenType.FALSE, "true": TokenType.TRUE,
        "fn": TokenType.FN, "let": TokenType.LET, "null": TokenType.NULL,
        "return": TokenType.RETURN, "while": TokenType.WHILE, "break": TokenType.BREAK,
        "continue": TokenType.CONTINUE, "print": TokenType.PRINT, "not": TokenType.NOT,
    }

    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def tokenize(self) -> list[Token]:
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        
        self.tokens.append(Token(TokenType.EOF, None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()
        match c:
            case '(': self.add_token(TokenType.LPAREN)
            case ')': self.add_token(TokenType.RPAREN)
            case '{': self.add_token(TokenType.LBRACE)
            case '}': self.add_token(TokenType.RBRACE)
            case '[': self.add_token(TokenType.LBRACKET)
            case ']': self.add_token(TokenType.RBRACKET)
            case ',': self.add_token(TokenType.COMMA)
            case '.': self.add_token(TokenType.DOT)
            case '-': self.add_token(TokenType.MINUS)
            case '+': self.add_token(TokenType.PLUS)
            case ';': self.add_token(TokenType.SEMICOLON)
            case '*': self.add_token(TokenType.STAR)
            case '%': self.add_token(TokenType.PERCENT)
            case '!': self.add_token(TokenType.BANGEQ if self.match('=') else TokenType.BANG)
            case '=': self.add_token(TokenType.EQEQ if self.match('=') else TokenType.EQ)
            case '<': self.add_token(TokenType.LTEQ if self.match('=') else TokenType.LT)
            case '>': self.add_token(TokenType.GTEQ if self.match('=') else TokenType.GT)
            case '/':
                if self.match('/'):
                    while self.peek() != '\n' and not self.is_at_end():
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            case ' ' | '\r' | '\t': pass
            case '\n': self.line += 1
            case '"': self.string()
            case _:
                if c.isdigit():
                    self.number()
                elif c.isalpha() or c == '_':
                    self.identifier()
                else:
                    raise LexError(self.line, f"Unexpected character: {c}")

    def string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n': self.line += 1
            self.advance()
        
        if self.is_at_end():
            raise LexError(self.line, "Unterminated string literal")
        
        self.advance() # Closing quote
        value = self.source[self.start + 1 : self.current - 1]
        self.add_token(TokenType.STRING, value)

    def number(self):
        while self.peek().isdigit(): self.advance()
        if self.peek() == '.' and self.peek_next().isdigit():
            self.advance() # consume .
            while self.peek().isdigit(): self.advance()
        
        value = float(self.source[self.start : self.current])
        self.add_token(TokenType.NUMBER, value)

    def identifier(self):
        while self.peek().isalnum() or self.peek() == '_': self.advance()
        text = self.source[self.start : self.current]
        type = self.KEYWORDS.get(text, TokenType.IDENTIFIER)
        self.add_token(type, text if type == TokenType.IDENTIFIER else None)

    def is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def advance(self) -> str:
        self.current += 1
        return self.source[self.current - 1]

    def add_token(self, type: TokenType, value: Any = None):
        self.tokens.append(Token(type, value, self.line))

    def match(self, expected: str) -> bool:
        if self.is_at_end(): return False
        if self.source[self.current] != expected: return False
        self.current += 1
        return True

    def peek(self) -> str:
        if self.is_at_end(): return '\0'
        return self.source[self.current]

    def peek_next(self) -> str:
        if self.current + 1 >= len(self.source): return '\0'
        return self.source[self.current + 1]
