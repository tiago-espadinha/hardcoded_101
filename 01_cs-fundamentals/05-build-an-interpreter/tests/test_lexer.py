import unittest
from lexer import Lexer, TokenType

class TestLexer(unittest.TestCase):
    def test_basic_tokens(self):
        source = "let x = 42;"
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        self.assertEqual(tokens[0].type, TokenType.LET)
        self.assertEqual(tokens[1].value, "x")
        self.assertEqual(tokens[3].value, 42.0)

if __name__ == "__main__":
    unittest.main()
