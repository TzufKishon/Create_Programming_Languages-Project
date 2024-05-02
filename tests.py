import unittest
import io
import sys
import contextlib
from Lexer import Lexer
from _Parser import Parser
from Interperter import Interpreter
from Token import Token
from AST import Assign

@contextlib.contextmanager
def capture_output():
    """Capture the output of sys.stdout and sys.stderr temporarily."""
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout  # This will be used to capture output for assertion
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestLanguageComponents(unittest.TestCase):
    def test_lexer_tokens(self):
        """Test lexer token generation to ensure correct token types are produced for a given input."""
        text = "let x = 100 + 50"
        lexer = Lexer(text)
        tokens = [lexer.get_next_token().type for _ in range(6)]  # Extract 6 tokens
        expected_tokens = [Token.LET, Token.IDENTIFIER, Token.ASSIGN, Token.INTEGER, Token.OPERATOR, Token.INTEGER]
        self.assertEqual(tokens, expected_tokens)

    def test_lexer_invalid_character(self):
        """Test the lexer with an invalid character to ensure it raises an exception as expected."""
        lexer = Lexer("#")
        with self.assertRaises(Exception):
            lexer.get_next_token()

    def test_parser_expression(self):
        """Test parsing of a simple assignment expression to ensure the AST is constructed correctly."""
        text = "x = 100 + 200"
        lexer = Lexer(text)
        parser = Parser(lexer)
        try:
            result = parser.parse()
            self.assertIsInstance(result[0], Assign)
            self.assertEqual(result[0].right.op.value, '+')
        except Exception as e:
            self.fail(f"Parser failed with error: {e}")

    def test_parser_syntax_error(self):
        """Test the parser with incomplete input to verify it raises a syntax error as expected."""
        text = "x = 100 +"
        lexer = Lexer(text)
        parser = Parser(lexer)
        with self.assertRaises(Exception):
            parser.parse()

    def test_interpreter_assignment(self):
        """Test the interpreter to ensure assignments are executed correctly and the scope is updated."""
        text = "let x = 100"
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.current_scope()['x'], 100)

    def test_interpreter_print(self):
        """Test the interpreter's handling of print statements to ensure output is captured correctly."""
        text = "print 123"
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        with capture_output() as output:
            interpreter.interpret()
            self.assertIn('123', output.getvalue())

if __name__ == '__main__':
    unittest.main()
