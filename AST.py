class AST:
    """Base class for all nodes in the Abstract Syntax Tree (AST).
    All specific AST node classes will inherit from this class.
    """
    pass

class BinOp(AST):
    """Represents a binary operation in the AST.
    
    Attributes:
        left (AST): The left child node, representing the left operand.
        op (Token): The operator token (e.g., '+', '-', '*', '/').
        right (AST): The right child node, representing the right operand.
    """
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(AST):
    """Represents a number in the AST.
    
    Attributes:
        token (Token): The token instance representing the number.
        value (int or float): The numeric value extracted from the token.
    """
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Var(AST):
    """Represents a variable in the AST.
    
    Attributes:
        token (Token): The token instance representing the variable's identifier.
        value (str): The name of the variable, extracted from the token.
    """
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Assign(AST):
    """Represents an assignment operation in the AST.
    
    Attributes:
        left (Var): The variable being assigned to.
        op (Token): The assignment operator token (e.g., '=').
        right (AST): The expression node whose value will be assigned to the variable.
    """
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Print(AST):
    """Represents a print operation in the AST.
    
    Attributes:
        value (AST): The expression whose value will be printed.
    """
    def __init__(self, value):
        self.value = value

class If(AST):
    """Represents an 'if' statement in the AST.
    
    Attributes:
        condition (AST): The condition expression which determines whether the 'if' body will execute.
        body (list of AST): The list of statement nodes that form the body of the 'if' statement.
    """
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class While(AST):
    """Represents a 'while' loop in the AST.
    
    Attributes:
        condition (AST): The condition expression which determines the continuation of the loop.
        body (list of AST): The list of statement nodes that form the body of the loop.
    """
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body