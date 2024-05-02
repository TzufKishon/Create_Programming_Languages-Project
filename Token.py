class Token:
    IF = 'IF'
    ENDIF = 'ENDIF'
    THEN = 'THEN'
    WHILE = 'WHILE'
    ENDWHILE = 'ENDWHILE'
    INTEGER = 'INTEGER'
    IDENTIFIER = 'IDENTIFIER'
    OPERATOR = 'OPERATOR'
    ASSIGN = 'ASSIGN'
    LET = 'LET'
    PRINT = 'PRINT'
    EOF = 'EOF' 

    def __init__(self, type_, value):
        """Initialize a new instance of Token.

        Args:
            type_ (str): The type of the token (e.g., 'INTEGER', 'IDENTIFIER').
            value (str or int): The value of the token, such as a variable name, literal number, or operator.

        Attributes:
            type (str): The category or type of the token as defined by the constants.
            value (str or int): The actual lexeme or value associated with the token.
        """
        self.type = type_
        self.value = value

    def __str__(self):
        """Return a string representation of the Token instance for easy debugging."""
        return f'Token({self.type}, {repr(self.value)})'

    def __repr__(self):
        """Return a formal string representation of the Token that can be used to recreate the object."""
        return self.__str__()
