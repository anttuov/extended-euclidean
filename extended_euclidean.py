# This script requires Python version 3.5 or higher and the NumPy library.
import math
import numpy as np

# Looking for the inverse of b in mod a, example values: a = 1155, b = 862 
a = 1155
b = 862
if a < 1 or b < 1 or type(a) is not int or type(b) is not int:
    exit("a and b must be positive integers")

if a < b:
    exit("a must be greater or equal to b")

gcd = math.gcd(a, b)
if gcd > 1:
    exit("gcd({},{}) > 1 => extended euclidean algorithm cannot be used.".format(a, b))


U = np.array([a, 1, 0])
V = np.array([b, 0, 1])
print("Input: U =", U, ", V =", V)

while V[0] > 0:
    W = U - math.floor(U[0] / V[0]) * V
    U = V
    V = W

x = U[1]
y = U[2]
inv = y % a  # the inverse of b

print("Result: U =", U, "\n")
# Test if the algorithm worked correctly and print the results
print("Testing if the algorithm worked as intended:")
test1 = U[0] == gcd
test2 = a * x + b * y == gcd
test3 = inv*b % a == 1

print("U(1) = gcd({},{}) = 1 || {}".format(a, b, test1))
print("x*a + y*b = ({}*{}) + ({}*{}) = {} || {}".format(x, a, y, b, a*x+b*y, test2))
print("{}*{} ≡ {} (mod {}) || {}".format(b, inv, (b*inv) % a, a, test3))

if test1 and test2 and test3:
    
    s = str(a).translate(str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉"))
    print("\nAlgorithm worked as expected, therefore:")
    print("{} ≡ {} (mod {})".format(y, inv, a))
    print("Result: {}⁻¹ = {} in Z{}".format(b, inv, s))
else:
    print("Something went wrong! :(")
