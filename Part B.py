from functools import reduce

#9
factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

print("Factorial of 5:", factorial(5))  # Expected output: 120

#10
concatenate = lambda l: '' if not l else l[0] + (' ' + concatenate(l[1:]) if len(l) > 1 else '')

print("Concatenated string:", concatenate(['Hello', 'world', 'from', 'lambda']))  # Expected output: 'Hello world from lambda'

#11
sum_squares = lambda lists: list(map(lambda l: reduce(lambda a, b: a + b, map(lambda x: x ** 2, filter(lambda y: y % 2 == 0, l)), 0), lists))

print("Sum of squares of even numbers:", sum_squares([[1, 2, 3], [4, 5, 6, 7, 8]]))  # Expected output: [4, 116]

#12
print(reduce(lambda acc, x: acc + x, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])), 0)) # Expected output: 56

#13
count_palindromes = lambda lists: list(map(lambda l: len(list(filter(lambda x: x == x[::-1], l))), lists))

print("Count of palindromes in each list:", count_palindromes([['radar', 'apple', 'level'], ['hello', 'racecar']]))  # Expected output: [2, 1]

#14
# "lazy evaluation" refers to the process of deferring the evaluation of expressions until their results are actually needed. This contrasts with eager evaluation, where expressions are evaluated as soon as they are defined.

# How Lazy Evaluation Works in the Program:

# The generator function generate_values() yields values one at a time. Instead of computing all its values upfront (as in eager evaluation), each value is generated only when the execution flow requires it.
# The list comprehension [square(x) for x in generate_values()] uses these yielded values immediately in the square() function. Here, each value is squared right at the moment it's yielded by the generator.
# This on-demand generation and processing mean that no intermediate storage or full list of generated values is needed beforehand. Each value is handled individually and directly as needed.

# Advantages in This Context:

# Memory Efficiency: Only the minimum necessary amount of data is held in memory at any time.
# Computational Efficiency: Computation happens exactly when needed and only for the data that is needed, which can speed up the initial response time and reduce unnecessary processing.
# Thus, lazy evaluation in this scenario allows the program to handle data more efficiently, reducing overhead and improving performance by dealing only with data as it becomes necessary to process it.

