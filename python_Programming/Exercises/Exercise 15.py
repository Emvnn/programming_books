# a. Concatenation of strings
result_a = 'Hello' + ', ' + 'World!'
print(result_a)  # Output: Hello, World!

# b. Repetition of string
result_b = 'Hello' * 3
print(result_b)  # Output: HelloHelloHello

# c. Multiplication of boolean values (True)
result_c = True * True
print(result_c)  # Output: 1

# d. Multiplication of boolean values (True and False)
result_d = True * False
print(result_d)  # Output: 0

# e. Multiplication of boolean value (False) with integer
result_e = False * 42
print(result_e)  # Output: 0

# f. Unary minus applied to boolean value (True)
try:
    result_f = -True
except TypeError as e:
    print(e)  # Output: bad operand type for unary -: 'bool'

# g. Addition of boolean values (True)
result_g = True + True
print(result_g)  # Output: 2
