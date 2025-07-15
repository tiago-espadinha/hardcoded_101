import ast_nodes as ast
from environment import Environment

class LumaRuntimeError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(f"[RuntimeError] {message}")

class BreakException(Exception): pass
class ContinueException(Exception): pass
class ReturnException(Exception):
    def __init__(self, value: any):
        self.value = value

class LumaFunction:
    def __init__(self, declaration: ast.FunctionDef, closure: Environment):
        self.declaration = declaration
        self.closure = closure

    def call(self, interpreter, arguments):
        env = Environment(self.closure)
        for i, param in enumerate(self.declaration.params):
            env.define(param, arguments[i])
        
        try:
            interpreter.execute_block(self.declaration.body.statements, env)
        except ReturnException as res:
            return res.value
        return None

class LumaArray:
    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        if not isinstance(index, (int, float)):
            raise LumaRuntimeError("Array index must be a number.")
        idx = int(index)
        if idx < 0 or idx >= len(self.elements):
            raise LumaRuntimeError("Array index out of bounds.")
        return self.elements[idx]

    def set(self, index, value):
        idx = int(index)
        self.elements[idx] = value

    def push(self, value):
        self.elements.append(value)
        return None

    def length(self):
        return float(len(self.elements))

    def __repr__(self):
        return f"[{', '.join(repr(e) for e in self.elements)}]"

class Interpreter:
    def __init__(self):
        self.globals = Environment()
        self.environment = self.globals

    def interpret(self, statements: list[ast.Statement]):
        try:
            for statement in statements:
                self.execute(statement)
        except LumaRuntimeError as error:
            print(error)

    def execute(self, node: ast.Node):
        if isinstance(node, ast.Expression):
            return self.evaluate(node)

        method_name = f"execute_{type(node).__name__}"
        visitor = getattr(self, method_name, self.generic_execute)
        return visitor(node)

    def generic_execute(self, stmt):
        raise NotImplementedError(f"No execute method for {type(stmt).__name__}")

    def evaluate(self, expr: ast.Expression):
        method_name = f"evaluate_{type(expr).__name__}"
        visitor = getattr(self, method_name, self.generic_evaluate)
        return visitor(expr)

    def generic_evaluate(self, expr):
        raise NotImplementedError(f"No evaluate method for {type(expr).__name__}")

    # Statements
    def execute_LetStatement(self, stmt: ast.LetStatement):
        value = self.evaluate(stmt.value)
        self.environment.define(stmt.name, value)

    def execute_PrintStatement(self, stmt: ast.PrintStatement):
        value = self.evaluate(stmt.expression)
        print(self.stringify(value))

    def execute_BlockStatement(self, stmt: ast.BlockStatement):
        self.execute_block(stmt.statements, Environment(self.environment))

    def execute_block(self, statements, env):
        previous = self.environment
        try:
            self.environment = env
            for statement in statements:
                self.execute(statement)
        finally:
            self.environment = previous

    def execute_IfStatement(self, stmt: ast.IfStatement):
        if self.is_truthy(self.evaluate(stmt.condition)):
            self.execute(stmt.then_block)
        else:
            executed = False
            for cond, block in stmt.elif_clauses:
                if self.is_truthy(self.evaluate(cond)):
                    self.execute(block)
                    executed = True
                    break
            if not executed and stmt.else_block:
                self.execute(stmt.else_block)

    def execute_WhileStatement(self, stmt: ast.WhileStatement):
        while self.is_truthy(self.evaluate(stmt.condition)):
            try:
                self.execute(stmt.body)
            except BreakException:
                break
            except ContinueException:
                continue

    def execute_BreakStatement(self, stmt: ast.BreakStatement):
        raise BreakException()

    def execute_ContinueStatement(self, stmt: ast.ContinueStatement):
        raise ContinueException()

    def execute_FunctionDef(self, stmt: ast.FunctionDef):
        function = LumaFunction(stmt, self.environment)
        self.environment.define(stmt.name, function)

    def execute_ReturnStatement(self, stmt: ast.ReturnStatement):
        value = None
        if stmt.value:
            value = self.evaluate(stmt.value)
        raise ReturnException(value)

    # Expressions
    def evaluate_NumberLiteral(self, expr: ast.NumberLiteral):
        return expr.value

    def evaluate_StringLiteral(self, expr: ast.StringLiteral):
        return expr.value

    def evaluate_BooleanLiteral(self, expr: ast.BooleanLiteral):
        return expr.value

    def evaluate_NullLiteral(self, expr: ast.NullLiteral):
        return None

    def evaluate_Identifier(self, expr: ast.Identifier):
        try:
            return self.environment.get(expr.name)
        except NameError as e:
            raise LumaRuntimeError(str(e))

    def evaluate_BinaryOp(self, expr: ast.BinaryOp):
        left = self.evaluate(expr.left)
        
        # Handle method calls/properties like arr.push or arr.length
        if expr.op == ".":
            if isinstance(left, LumaArray):
                method_name = expr.right.name if isinstance(expr.right, ast.Identifier) else None
                if method_name == "push":
                    return left.push
                if method_name == "length":
                    return left.length()
            if isinstance(left, str) and isinstance(expr.right, ast.Identifier) and expr.right.name == "length":
                return float(len(left))
            raise LumaRuntimeError(f"Property '{expr.right}' not found.")

        right = self.evaluate(expr.right)

        match expr.op:
            case "+":
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return left + right
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                raise LumaRuntimeError("Operands must be numbers or strings.")
            case "-": return left - right
            case "*": return left * right
            case "/": return left / right
            case "%": return left % right
            case ">": return left > right
            case ">=": return left >= right
            case "<": return left < right
            case "<=": return left <= right
            case "==": return left == right
            case "!=": return left != right
        return None

    def evaluate_UnaryOp(self, expr: ast.UnaryOp):
        right = self.evaluate(expr.operand)
        if expr.op == "-": return -right
        if expr.op == "not": return not self.is_truthy(right)
        return None

    def evaluate_LogicalOp(self, expr: ast.LogicalOp):
        left = self.evaluate(expr.left)
        if expr.op == "or":
            if self.is_truthy(left): return left
        else: # and
            if not self.is_truthy(left): return left
        return self.evaluate(expr.right)

    def evaluate_Grouping(self, expr: ast.Grouping):
        return self.evaluate(expr.expression)

    def evaluate_AssignStatement(self, expr: ast.AssignStatement):
        value = self.evaluate(expr.value)
        try:
            self.environment.assign(expr.name, value)
        except NameError as e:
            raise LumaRuntimeError(str(e))
        return value

    def evaluate_FunctionCall(self, expr: ast.FunctionCall):
        callee = self.evaluate(expr.callee)
        arguments = [self.evaluate(arg) for arg in expr.args]
        
        if callable(callee): # Built-in or method
            return callee(*arguments)
        
        if not isinstance(callee, LumaFunction):
            raise LumaRuntimeError("Can only call functions and methods.")
        
        if len(arguments) != len(callee.declaration.params):
            raise LumaRuntimeError(f"Expected {len(callee.declaration.params)} arguments but got {len(arguments)}.")
            
        return callee.call(self, arguments)

    def evaluate_ArrayLiteral(self, expr: ast.ArrayLiteral):
        return LumaArray([self.evaluate(el) for el in expr.elements])

    def evaluate_IndexExpression(self, expr: ast.IndexExpression):
        array = self.evaluate(expr.array)
        index = self.evaluate(expr.index)
        
        if isinstance(array, LumaArray):
            return array.get(index)
        if isinstance(array, str):
            idx = int(index)
            if idx < 0 or idx >= len(array):
                raise LumaRuntimeError("String index out of bounds.")
            return array[idx]
        
        raise LumaRuntimeError("Only arrays and strings support indexing.")

    # Utils
    def is_truthy(self, value):
        if value is None: return False
        if isinstance(value, bool): return value
        return True

    def stringify(self, value):
        if value is None: return "null"
        if isinstance(value, bool): return str(value).lower()
        if isinstance(value, float):
            text = str(value)
            if text.endswith(".0"): text = text[:-2]
            return text
        return str(value)
