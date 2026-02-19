a = 12 # Assigment Operator
b = 5

# Arithmetic Operators
print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division : always gives answer in float for true division
print(a // b) # Floor Division : rounds to lowest integer
print(a % b) # Modulo
print(a ** b) # Exponentiation

# Compound Assigment Operators
a += 8 # a = a + 8
b -= 3
print(a, b)
a **= b
b /= a
print(a, b)

c = 5
d = 3
print(c, d)
c = c + d # Swapping two var with only operations
d = c - d
c = c - d
print(c, d)

# Relational Operators
a = 35
b = 40
a > b # Greater than
a < b # Smaller than
a == b # Equal to
a != b # Not Equal to
a >= b # Greater OR Equal to
a <= b # Smaller OR Equal to

# Logical Operators
a = 8
b = 12
print(a > 5 and a < 10) # AND : True, if Both are true
print(b > 5 or b < 10) # OR : True, if Either is true
print(not(a > 5)) # NOT : Reverse the Result

"""Operator Precedence
Most operators are Left-Associative like +, -, *
Operators with Right-Associative are **"""
print(10 / 2 * 3)
print(2 ** 2 ** 3)