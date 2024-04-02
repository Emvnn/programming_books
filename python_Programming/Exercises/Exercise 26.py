Write a function which takes two numeric arguments, one named
subtotal and the other named tax_rate, and calculates and returns the
total including tax. For example, if the arguments supplied were 114.0
for subtotal and 0.05 for tax_rate, your function should return the value
119.7. If the arguments were 328.0 and 0.045, your function should return the value 342.76.
This function should produce no side effects.

---------

def calculate_total(subtotal, tax_rate):
    total = subtotal * (1 + tax_rate)
    return total

# Example usage
result = calculate_total(114.0, 0.05)
print(result)  # Output: 119.7

result = calculate_total(328.0, 0.045)
print(result)  # Output: 342.76

