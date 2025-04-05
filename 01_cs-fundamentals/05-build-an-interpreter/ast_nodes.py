from dataclasses import dataclass
from typing import Any, List, Optional

@dataclass
class Node:
    pass

@dataclass
class Statement(Node):
    pass

@dataclass
class Expression(Node):
    pass

@dataclass
class NumberLiteral(Expression):
    value: float

@dataclass
class StringLiteral(Expression):
    value: str

@dataclass
class BooleanLiteral(Expression):
    value: bool

@dataclass
class NullLiteral(Expression):
    pass

@dataclass
class Identifier(Expression):
    name: str

@dataclass
class BinaryOp(Expression):
    left: Expression
    op: str
    right: Expression

@dataclass
class UnaryOp(Expression):
    op: str
    operand: Expression

@dataclass
class LogicalOp(Expression):
    left: Expression
    op: str
    right: Expression

@dataclass
class Grouping(Expression):
    expression: Expression

@dataclass
class LetStatement(Statement):
    name: str
    value: Expression

@dataclass
class AssignStatement(Expression):
    name: str
    value: Expression

@dataclass
class PrintStatement(Statement):
    expression: Expression

@dataclass
class BlockStatement(Statement):
    statements: List[Statement]

@dataclass
class IfStatement(Statement):
    condition: Expression
    then_block: BlockStatement
    elif_clauses: List[tuple[Expression, BlockStatement]]
    else_block: Optional[BlockStatement]

@dataclass
class WhileStatement(Statement):
    condition: Expression
    body: BlockStatement

@dataclass
class BreakStatement(Statement):
    pass

@dataclass
class ContinueStatement(Statement):
    pass

@dataclass
class FunctionDef(Statement):
    name: str
    params: List[str]
    body: BlockStatement

@dataclass
class ReturnStatement(Statement):
    value: Optional[Expression]

@dataclass
class FunctionCall(Expression):
    callee: Expression
    args: List[Expression]

@dataclass
class ArrayLiteral(Expression):
    elements: List[Expression]

@dataclass
class IndexExpression(Expression):
    array: Expression
    index: Expression
