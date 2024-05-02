"""
BNF:
<program> ::= {<statement>}

<statement> ::= <assignment_statement> | <print_statement> | <if_statement> | <while_statement>

<assignment_statement> ::= "let" <identifier> "=" <expression> 
                          | <identifier> "=" <expression>

<print_statement> ::= "print" <expression>

<if_statement> ::= "if" <comparison> "then" <block> "endif"

<while_statement> ::= "while" <comparison> "then" <block> "endwhile"

<block> ::= {<statement>}

<expression> ::= <term> {("+" | "-") <term>}

<term> ::= <factor> {("*" | "/") <factor>}

<factor> ::= <integer> | <identifier> | "(" <expression> ")"

<comparison> ::= <expression> {("<" | ">" | "==") <expression>}

<identifier> ::= [a-zA-Z_][a-zA-Z0-9_]*

<integer> ::= [0-9]+
"""

from Token import Token

class Lexer:
    def __init__(self, text):
        """Initialize the Lexer with the source code as text.
        
        Args:
            text (str): The string of source code to tokenize.
        
        Attributes:
            text (str): Stores the entire source code as a string.
            pos (int): Current position in the text (character index).
            current_char (str or None): Character at the current position or None if at end of text.
        """
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def error(self):
        """Raise an exception indicating an error at the current lexer position."""
        context = self.text[max(0, self.pos-10):self.pos+10]
        raise Exception(f"Invalid character: '{self.current_char}' at position {self.pos}, context '{context}'")

    def advance(self):
        """Advance the `pos` pointer to the next character in the text.
        Update `current_char` to the new character at the current position.
        """
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        """Skip any whitespace characters in the input until a non-whitespace character is encountered."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Parse a sequence of digits into an integer and return it."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def identifier(self):
        """Parse identifiers and reserved keywords into tokens."""
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        keyword_map = {
            'let': Token.LET,
            'print': Token.PRINT,
            'if': Token.IF,
            'then': Token.THEN,
            'endif': Token.ENDIF,
            'while': Token.WHILE,
            'endwhile': Token.ENDWHILE
        }
        return Token(keyword_map.get(result.lower(), Token.IDENTIFIER), result)

    def get_next_token(self):
        """Tokenize the input one token at a time by analyzing the current character."""
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(Token.INTEGER, self.integer())

            if self.current_char.isalpha() or self.current_char == '_':
                return self.identifier()

            if self.current_char in '+-*/()':
                op_char = self.current_char
                self.advance()
                return Token(Token.OPERATOR, op_char)

            if self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(Token.OPERATOR, '==')
                return Token(Token.ASSIGN, '=')

            if self.current_char == '>':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(Token.OPERATOR, '>=')
                return Token(Token.OPERATOR, '>')

            if self.current_char == '<':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(Token.OPERATOR, '<=')
                return Token(Token.OPERATOR, '<')

            self.error()

        return Token(Token.EOF, None)  
