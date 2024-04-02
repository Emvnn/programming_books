The following Python code runs perfectly fine but deviates from the PEP
8 style guide. Using your chosen IDE, fix the issues and check to make
sure that the program still runs correctly.
def CIRCUMFERENCEOFCIRCLE(radius):
c=2*pi*radius
return c
pi=3.14159
CIRC=CIRCUMFERENCEOFCIRCLE(22)
print("The circumference of a circle with a radius of 22cm"
"is "+str(CIRC)+ "cm.")

--------

import math

def circumference_of_circle(radius):
    c = 2 * math.pi * radius
    return c

pi = 3.14159
circ = circumference_of_circle(22)
print("The circumference of a circle with a radius of 22cm is " + str(circ) + "cm.")

