from _Parser import Parser
from Lexer import Lexer

class Interpreter:
    def __init__(self, parser):
        """Initialize the Interpreter with a parser instance.
        
        Args:
            parser (Parser): An instance of a parser that produces an AST from source code.
        
        Attributes:
            scopes (list of dict): A list of dictionary objects, each representing a variable scope.
                                   Initializes with a single global scope.
        """
        self.parser = parser
        self.scopes = [{}]  

    def current_scope(self):
        """Return the dictionary representing the current variable scope."""
        return self.scopes[-1]

    def enter_scope(self):
        """Create a new, nested scope by copying the current scope into a new layer."""
        self.scopes.append(dict(self.current_scope()))

    def exit_scope(self):
        """Exit the current scope and revert to the parent scope, with updates to any changed values."""
        exited_scope = self.scopes.pop()
        if self.scopes:
            parent_scope = self.current_scope()
            for key, value in exited_scope.items():
                if key in parent_scope:
                    parent_scope[key] = value

    def visit(self, node):
        """General visit method that dispatches to node-specific methods based on node type.
        
        Args:
            node (AST): The AST node to visit.
        
        Returns:
            The result of the visited node or raises an exception if no method is available.
        """
        if isinstance(node, list):
            return [self.visit(n) for n in node]
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.no_visit_method)
        return visitor(node)

    def no_visit_method(self, node):
        """Handle visits to undefined node types by raising an exception."""
        raise Exception(f"No visitor method defined for {type(node).__name__}")

    def visit_Num(self, node):
        """Return the numeric value from a Num node."""
        return node.value

    def visit_Var(self, node):
        """Retrieve the value of a variable from the scopes stack, if defined."""
        var_name = node.value
        for scope in reversed(self.scopes):
            if var_name in scope:
                return scope[var_name]
        raise NameError(f"Variable '{var_name}' not defined")

    def visit_BinOp(self, node):
        """Evaluate a binary operation by visiting the left and right operands and applying the operator."""
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)
        if node.op.value == '+':
            return left_val + right_val
        elif node.op.value == '-':
            return left_val - right_val
        elif node.op.value == '*':
            return left_val * right_val
        elif node.op.value == '/':
            return left_val // right_val  
        elif node.op.value == '==':
            return left_val == right_val
        elif node.op.value == '>':
            return left_val > right_val
        elif node.op.value == '<':
            return left_val < right_val
        else:
            raise ValueError(f"Unsupported operator '{node.op.value}'")

    def visit_Assign(self, node):
        """Execute an assignment by updating the current scope with the new value."""
        var_name = node.left.value
        new_value = self.visit(node.right)
        self.current_scope()[var_name] = new_value
        return new_value

    def visit_While(self, node):
        """Execute a while loop by repeatedly checking the condition and executing the body in a new scope."""
        while True:
            condition_result = self.visit(node.condition)
            if not condition_result:
                break
            self.enter_scope()
            self.visit(node.body)
            self.exit_scope()

    def visit_If(self, node):
        """Execute an if statement by evaluating the condition and executing the body if true."""
        condition_result = self.visit(node.condition)
        if condition_result:
            return self.visit(node.body)

    def visit_Print(self, node):
        """Print the result of evaluating the expression contained in a Print node."""
        print(self.visit(node.value))

    def interpret(self):
        """Interpret the entire program by parsing and then visiting the AST."""
        tree = self.parser.parse()
        return self.visit(tree)

if __name__ == "__main__":
    text = """
    let balance = 1000
    let withdrawal = 100
    let counter = 0

    while counter < 10 THEN
        print balance
        if balance > 200 THEN
            let balance = balance - withdrawal
            print 1
            print balance
            if balance < 500 THEN
                print 2
                if balance < 300 THEN
                    print 3
                ENDIF
            ENDIF
        ENDIF
        let counter = counter + 1
    """
    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    interpreter.interpret()
