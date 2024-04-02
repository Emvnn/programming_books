Some operands don’t work with certain types. For example, the following
will result in errors. Try these out at a prompt, and observe what happens.
Make a note of the type of error which occurs.
a. 'Hello' / 3
b. -'Hello'
c. 'Hello' - 'H'

-------

# a. Division of a string by an integer
try:
    result_a = 'Hello' / 3
except TypeError as e:
    print(e)  # Output: unsupported operand type(s) for /: 'str' and 'int'

# b. Unary minus applied to a string
try:
    result_b = -'Hello'
except TypeError as e:
    print(e)  # Output: bad operand type for unary -: 'str'

# c. Subtraction of strings
try:
    result_c = 'Hello' - 'H'
except TypeError as e:
    print(e)  # Output: unsupported operand type(s) for -: 'str' and 'str'

