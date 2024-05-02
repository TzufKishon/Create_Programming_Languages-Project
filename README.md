# Python Interpreter

This project is a simple interpreter implemented in Python, designed to parse and evaluate a subset of a custom programming language. The interpreter handles basic arithmetic operations, control structures such as conditional statements and loops, and supports variable assignments.

## Features

- **Arithmetic Operations**: Supports basic arithmetic operations including addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Comparison Operators**: Handles comparison for conditional logic with operators like greater than (`>`), less than (`<`), and equals (`==`).
- **Control Structures**: Includes support for `if` statements and `while` loops to manage flow control.
- **Variable Management**: Allows variable assignments and maintains variable values across different scopes within a program.
- **Error Handling**: Robust error reporting for syntax and runtime errors to aid debugging.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Simple-Python-Interpreter.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Simple-Python-Interpreter
   ```

## Usage

Run the interpreter using Python. Once running, the interpreter allows you to input expressions and commands directly:

```bash
python main.py
```

### Example Session
Here's how you can use the interpreter in a typical session:

```
>>> let a = 10
>>> let b = 20
>>> print a + b
30
>>> if a > b then:
...     print a
... else:
...     print b
...
20
>>> while a < 15 then:
...     let a = a + 1
...     print a
...
11
12
13
14
15
```

To exit the interpreter, you can simply type `exit()`.

## Syntax

The interpreter follows a straightforward syntax for expressions, variable assignments, and control structures:

- **Expressions** involve arithmetic operations or variable references.
- **Statements** include assignments, print statements, and control structures.
- **Control Structures** like `if` and `while` manage the flow of execution based on conditions.
- **Variables** can be declared and used throughout the program using the `let` keyword.

## License

This project is released under the MIT License, allowing for flexibility and reuse with appropriate credit.

## Acknowledgements

This interpreter project is inspired by classical compiler design principles and is greatly influenced by resources and tutorials on modern interpreting techniques. Thanks to numerous open-source projects and community forums for providing insights and foundational concepts in language design and interpretation.

---

For any issues or contributions, please visit the repository's issues section or submit a pull request. Enjoy experimenting with the Simple Python Interpreter!
