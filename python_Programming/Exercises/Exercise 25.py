a. Write a function which take an integer as an argument and returns 0
if the integer is even and 1 if the integer is odd. Hint: The remainder
(modulo) operator, %, calculates the remainder when performing
integer division. For example, 17 % 5 yields 2, because 5 goes into
17 three times, leaving a remainder of two.
b. What did you name your function and why?

---------

def check_even_or_odd(num):
    if num % 2 == 0:
        return 0  # Even
    else:
        return 1  # Odd

# Example usage
result = check_even_or_odd(5)
print(result)  # Output: 1


- I named the function check_even_or_odd because it clearly indicates the purpose of the function, which is to check whether the given integer is even or odd.
