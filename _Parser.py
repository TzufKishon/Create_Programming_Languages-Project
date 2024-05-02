from Token import Token
from AST import *

class Parser:
    def __init__(self, lexer):
        """Initialize the Parser with a lexer object. The lexer will tokenize the input for the parser to analyze."""
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, message="Syntax error"):
        """Raise an exception for syntax errors with a given message."""
        raise Exception(message)

    def eat(self, token_type):
        """Consume the current token if it matches token_type; otherwise, raise a syntax error."""
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Expected token {token_type}, but found {self.current_token.type}")

    def factor(self):
        """Parse a factor which can be an integer, a variable, or an expression enclosed in parentheses."""
        token = self.current_token
        if token.type == Token.INTEGER:
            self.eat(Token.INTEGER)
            return Num(token)
        elif token.type == Token.IDENTIFIER:
            self.eat(Token.IDENTIFIER)
            return Var(token)
        elif token.value == '(':
            self.eat(Token.OPERATOR)
            node = self.expression()
            self.eat(Token.OPERATOR)
            return node
        else:
            self.error("Invalid syntax in factor")

    def term(self):
        """Parse terms that involve multiplication or division of factors."""
        node = self.factor()
        while self.current_token.value in ('*', '/'):
            token = self.current_token
            self.eat(Token.OPERATOR)
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def expression(self):
        """Parse expressions that involve addition or subtraction of terms."""
        node = self.term()
        while self.current_token.value in ('+', '-'):
            token = self.current_token
            self.eat(Token.OPERATOR)
            node = BinOp(left=node, op=token, right=self.term())
        return node

    def comparison(self):
        """Parse comparison operators (>, <, ==) between expressions."""
        node = self.expression()
        while self.current_token.type == Token.OPERATOR and self.current_token.value in ('>', '<', '=='):
            token = self.current_token
            self.eat(Token.OPERATOR)
            node = BinOp(left=node, op=token, right=self.expression())
        return node

    def assignment_statement(self):
        """Parse assignment statements for variables."""
        self.eat(Token.LET)
        var_token = self.current_token
        self.eat(Token.IDENTIFIER)
        self.eat(Token.ASSIGN)
        expr = self.expression()
        return Assign(left=Var(var_token), op=Token(Token.ASSIGN, '='), right=expr)

    def print_statement(self):
        """Parse print statements that output the value of expressions."""
        self.eat(Token.PRINT)
        expr = self.comparison()
        return Print(value=expr)

    def if_statement(self):
        """Parse if statements, including the condition and the body enclosed by THEN and ENDIF."""
        try:
            self.eat(Token.IF)
            condition = self.comparison()
            if condition is None:
                raise ValueError("Failed to parse condition in IF statement.")
            self.eat(Token.THEN)
            body = self.block()
            if body is None:
                raise ValueError("Failed to parse body in IF statement.")
            if self.current_token.type == Token.ENDIF:
                self.eat(Token.ENDIF)
            else:
                self.error("Expected ENDIF")
            return If(condition=condition, body=body)

        except Exception as e:
            print(f"Error parsing IF statement: {str(e)}")
            raise

    def block(self):
        """Parse a block of statements until the end of the block is reached (e.g., ENDWHILE, ENDIF)."""
        statements = []
        while self.current_token.type != Token.EOF and self.current_token.type not in (Token.ENDWHILE, Token.ENDIF):
            stmt = self.statement()
            if stmt is not None:
                statements.append(stmt)
            else:
                self.error("Unexpected None statement")
        return statements

    def while_statement(self):
        """Parse while statements that execute a block repeatedly as long as a condition is true."""
        self.eat(Token.WHILE)
        condition = self.comparison()
        self.eat(Token.THEN)
        body = self.block()
        return While(condition=condition, body=body)

    def statement(self):
        """Dispatch parsing to specific statement types based on the current token."""
        if self.current_token.type == Token.LET:
            self.eat(Token.LET)
            var_token = self.current_token
            self.eat(Token.IDENTIFIER)
            self.eat(Token.ASSIGN)
            expr = self.expression()
            return Assign(left=Var(var_token), op=Token(Token.ASSIGN, '='), right=expr)

        elif self.current_token.type == Token.IDENTIFIER:
            var_token = self.current_token
            self.eat(Token.IDENTIFIER)
            if self.current_token.type == Token.ASSIGN:
                self.eat(Token.ASSIGN)
                expr = self.expression()
                return Assign(Var(var_token), '=', expr)
            else:
                self.error(f"Expected assignment after identifier {var_token.value}")

        elif self.current_token.type == Token.PRINT:
            self.eat(Token.PRINT)
            expr = self.expression()
            return Print(expr)

        elif self.current_token.type == Token.WHILE:
            self.eat(Token.WHILE)
            condition = self.comparison()
            self.eat(Token.THEN)
            body = self.block()
            return While(condition=condition, body=body)

        elif self.current_token.type == Token.IF:
            self.eat(Token.IF)
            condition = self.comparison()
            self.eat(Token.THEN)
            body = self.block()
            if self.current_token.type == Token.ENDIF:
                self.eat(Token.ENDIF)
            else:
                self.error("Expected 'ENDIF' after the block")
            return If(condition=condition, body=body)

        else:
            self.error(f"Unrecognized statement with token {self.current_token.type} and value {self.current_token.value}")

    def program(self):
        """Parse the entire program consisting of multiple statements."""
        results = []
        while self.current_token.type != Token.EOF:
            results.append(self.statement())
        return results

    def parse(self):
        """Start the parsing process of the entire program and return the results."""
        return self.program()