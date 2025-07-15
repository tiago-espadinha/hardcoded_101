from lexer import Token, TokenType
import ast_nodes as ast

class ParseError(Exception):
    def __init__(self, token: Token, message: str):
        self.token = token
        self.message = message
        line = token.line if token else "EOF"
        super().__init__(f"[ParseError line {line}] {message}")

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self) -> list[ast.Statement]:
        statements = []
        while not self.is_at_end():
            statements.append(self.declaration())
        return statements

    # Statement parsing
    def declaration(self):
        try:
            if self.match(TokenType.LET): return self.let_declaration()
            if self.match(TokenType.FN): return self.function_declaration()
            return self.statement()
        except ParseError as error:
            self.synchronize()
            return None

    def let_declaration(self):
        name = self.consume(TokenType.IDENTIFIER, "Expect variable name.").value
        self.consume(TokenType.EQ, "Expect '=' after variable name.")
        value = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after variable declaration.")
        return ast.LetStatement(name, value)

    def function_declaration(self):
        name = self.consume(TokenType.IDENTIFIER, "Expect function name.").value
        self.consume(TokenType.LPAREN, "Expect '(' after function name.")
        params = []
        if not self.check(TokenType.RPAREN):
            while True:
                params.append(self.consume(TokenType.IDENTIFIER, "Expect parameter name.").value)
                if not self.match(TokenType.COMMA): break
        self.consume(TokenType.RPAREN, "Expect ')' after parameters.")
        self.consume(TokenType.LBRACE, "Expect '{' before function body.")
        body = self.block()
        return ast.FunctionDef(name, params, body)

    def statement(self):
        if self.match(TokenType.IF): return self.if_statement()
        if self.match(TokenType.PRINT): return self.print_statement()
        if self.match(TokenType.WHILE): return self.while_statement()
        if self.match(TokenType.RETURN): return self.return_statement()
        if self.match(TokenType.BREAK):
            self.consume(TokenType.SEMICOLON, "Expect ';' after 'break'.")
            return ast.BreakStatement()
        if self.match(TokenType.CONTINUE):
            self.consume(TokenType.SEMICOLON, "Expect ';' after 'continue'.")
            return ast.ContinueStatement()
        if self.match(TokenType.LBRACE): return self.block()
        return self.expression_statement()

    def if_statement(self):
        self.consume(TokenType.LPAREN, "Expect '(' after 'if'.")
        condition = self.expression()
        self.consume(TokenType.RPAREN, "Expect ')' after if condition.")
        then_block = self.block() if self.check(TokenType.LBRACE) else ast.BlockStatement([self.statement()])
        
        elif_clauses = []
        while self.match(TokenType.ELSE) and self.match(TokenType.IF):
            self.consume(TokenType.LPAREN, "Expect '(' after 'else if'.")
            elif_cond = self.expression()
            self.consume(TokenType.RPAREN, "Expect ')' after else if condition.")
            elif_block = self.block() if self.check(TokenType.LBRACE) else ast.BlockStatement([self.statement()])
            elif_clauses.append((elif_cond, elif_block))
        
        else_block = None
        if self.previous().type == TokenType.ELSE or self.match(TokenType.ELSE):
            else_block = self.block() if self.check(TokenType.LBRACE) else ast.BlockStatement([self.statement()])
            
        return ast.IfStatement(condition, then_block, elif_clauses, else_block)

    def while_statement(self):
        self.consume(TokenType.LPAREN, "Expect '(' after 'while'.")
        condition = self.expression()
        self.consume(TokenType.RPAREN, "Expect ')' after while condition.")
        body = self.block() if self.check(TokenType.LBRACE) else ast.BlockStatement([self.statement()])
        return ast.WhileStatement(condition, body)

    def return_statement(self):
        value = None
        if not self.check(TokenType.SEMICOLON):
            value = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after return value.")
        return ast.ReturnStatement(value)

    def print_statement(self):
        self.consume(TokenType.LPAREN, "Expect '(' after 'print'.")
        value = self.expression()
        self.consume(TokenType.RPAREN, "Expect ')' after print value.")
        self.consume(TokenType.SEMICOLON, "Expect ';' after print statement.")
        return ast.PrintStatement(value)

    def block(self):
        self.match(TokenType.LBRACE) # consume { if we haven't already
        statements = []
        while not self.check(TokenType.RBRACE) and not self.is_at_end():
            statements.append(self.declaration())
        self.consume(TokenType.RBRACE, "Expect '}' after block.")
        return ast.BlockStatement(statements)

    def expression_statement(self):
        expr = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after expression.")
        return expr

    # Expression parsing (Precedence Climbing)
    def expression(self):
        return self.assignment()

    def assignment(self):
        expr = self.logical_or()
        if self.match(TokenType.EQ):
            equals = self.previous()
            value = self.assignment()
            if isinstance(expr, ast.Identifier):
                return ast.AssignStatement(expr.name, value)
            raise ParseError(equals, "Invalid assignment target.")
        return expr

    def logical_or(self):
        expr = self.logical_and()
        while self.match(TokenType.OR):
            op = self.previous().type
            right = self.logical_and()
            expr = ast.LogicalOp(expr, "or", right)
        return expr

    def logical_and(self):
        expr = self.equality()
        while self.match(TokenType.AND):
            op = self.previous().type
            right = self.equality()
            expr = ast.LogicalOp(expr, "and", right)
        return expr

    def equality(self):
        expr = self.comparison()
        while self.match(TokenType.EQEQ, TokenType.BANGEQ):
            op = "==" if self.previous().type == TokenType.EQEQ else "!="
            right = self.comparison()
            expr = ast.BinaryOp(expr, op, right)
        return expr

    def comparison(self):
        expr = self.term()
        while self.match(TokenType.GT, TokenType.GTEQ, TokenType.LT, TokenType.LTEQ):
            op = self.previous()
            right = self.term()
            expr = ast.BinaryOp(expr, self.token_to_op(op.type), right)
        return expr

    def term(self):
        expr = self.factor()
        while self.match(TokenType.PLUS, TokenType.MINUS):
            op = "+" if self.previous().type == TokenType.PLUS else "-"
            right = self.factor()
            expr = ast.BinaryOp(expr, op, right)
        return expr

    def factor(self):
        expr = self.unary()
        while self.match(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT):
            op = self.previous()
            right = self.unary()
            expr = ast.BinaryOp(expr, self.token_to_op(op.type), right)
        return expr

    def unary(self):
        if self.match(TokenType.BANG, TokenType.MINUS, TokenType.NOT):
            op = "not" if self.previous().type in (TokenType.BANG, TokenType.NOT) else "-"
            right = self.unary()
            return ast.UnaryOp(op, right)
        return self.call()

    def call(self):
        expr = self.primary()
        while True:
            if self.match(TokenType.LPAREN):
                expr = self.finish_call(expr)
            elif self.match(TokenType.LBRACKET):
                index = self.expression()
                self.consume(TokenType.RBRACKET, "Expect ']' after index.")
                expr = ast.IndexExpression(expr, index)
            elif self.match(TokenType.DOT):
                name = self.consume(TokenType.IDENTIFIER, "Expect property name after '.'.").value
                # In Luma, .push and .length are handled as special method calls or properties
                # For simplicity, we'll treat them as identifiers for now and handle in interpreter
                expr = ast.BinaryOp(expr, ".", ast.Identifier(name))
            else:
                break
        return expr

    def finish_call(self, callee):
        args = []
        if not self.check(TokenType.RPAREN):
            while True:
                args.append(self.expression())
                if not self.match(TokenType.COMMA): break
        self.consume(TokenType.RPAREN, "Expect ')' after arguments.")
        return ast.FunctionCall(callee, args)

    def primary(self):
        if self.match(TokenType.FALSE): return ast.BooleanLiteral(False)
        if self.match(TokenType.TRUE): return ast.BooleanLiteral(True)
        if self.match(TokenType.NULL): return ast.NullLiteral()
        if self.match(TokenType.NUMBER): return ast.NumberLiteral(self.previous().value)
        if self.match(TokenType.STRING): return ast.StringLiteral(self.previous().value)
        if self.match(TokenType.IDENTIFIER): return ast.Identifier(self.previous().value)
        if self.match(TokenType.LPAREN):
            expr = self.expression()
            self.consume(TokenType.RPAREN, "Expect ')' after expression.")
            return ast.Grouping(expr)
        if self.match(TokenType.LBRACKET):
            elements = []
            if not self.check(TokenType.RBRACKET):
                while True:
                    elements.append(self.expression())
                    if not self.match(TokenType.COMMA): break
            self.consume(TokenType.RBRACKET, "Expect ']' after array elements.")
            return ast.ArrayLiteral(elements)
        
        raise ParseError(self.peek(), "Expect expression.")

    # Helpers
    def match(self, *types) -> bool:
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False

    def check(self, type) -> bool:
        if self.is_at_end(): return False
        return self.peek().type == type

    def advance(self) -> Token:
        if not self.is_at_end(): self.current += 1
        return self.previous()

    def is_at_end(self) -> bool:
        return self.peek().type == TokenType.EOF

    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def consume(self, type, message):
        if self.check(type): return self.advance()
        raise ParseError(self.peek(), message)

    def token_to_op(self, type):
        return {
            TokenType.PLUS: "+", TokenType.MINUS: "-", TokenType.STAR: "*",
            TokenType.SLASH: "/", TokenType.PERCENT: "%", TokenType.EQEQ: "==",
            TokenType.BANGEQ: "!=", TokenType.GT: ">", TokenType.GTEQ: ">=",
            TokenType.LT: "<", TokenType.LTEQ: "<=", TokenType.DOT: "."
        }.get(type)

    def synchronize(self):
        self.advance()
        while not self.is_at_end():
            if self.previous().type == TokenType.SEMICOLON: return
            if self.peek().type in (TokenType.FN, TokenType.LET, TokenType.IF, 
                                    TokenType.WHILE, TokenType.PRINT, TokenType.RETURN):
                return
            self.advance()
