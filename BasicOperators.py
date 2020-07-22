## Basic Operators ##
# Operators are the constructs which can manipulate the value of operands.
# Types of Operator: Python language supports the following types of operators.
# Arithmetic Operators
# Comparison (Relational) Operators
# Assignment Operators
# Logical Operators
# Bitwise Operators
# Membership Operators
# Identity Operators

## Python Arithmetic Operators ##

a = 9
b = 2

add = a + b  # Addition
sub = a - b  # Subtraction
div = a / b  # Division
mul = a * b  # Multiplication
mod = a % b  # Modulus
exp = a ** b  # Exponent
floordiv = a // b  # Floor Division

print(add)
print(sub)
print(div)
print(mul)
print(mod)
print(exp)
print(floordiv)

## Python Comparison Operators ##
# These operators compare the values on either sides of them and decide the relation among them.
# They are also called Relational operators.

a = 21
b = 10
c = 0

if a == b:
    print("Line 1 - a is equal to b")
else:
    print("Line 1 - a is not equal to b")

if a != b:
    print("Line 2 - a is not equal to b")
else:
    print("Line 2 - a is equal to b")

if a < b:
    print("Line 4 - a is less than b")
else:
    print("Line 4 - a is not less than b")

if a > b:
    print("Line 5 - a is greater than b")
else:
    print("Line 5 - a is not greater than b")

a = 5
b = 20

if a <= b:
    print("Line 6 - a is either less than or equal to  b")
else:
    print("Line 6 - a is neither less than nor equal to  b")

if b >= a:
    print("Line 7 - b is either greater than  or equal to b")
else:
    print("Line 7 - b is neither greater than  nor equal to b")

## Python Assignment Operators ##


a = 21
b = 10
c = 0

c = a + b
print("Line 1 - Value of c is ", c)

c += a  # c += a is equivalent to c = c + a
print("Line 2 - Value of c is ", c)

c *= a  # c *= a is equivalent to c = c * a
print("Line 3 - Value of c is ", c)

c /= a  # c /= a is equivalent to c = c / a
print("Line 4 - Value of c is ", c)

c = 2
c %= a  # c %= a is equivalent to c = c % a
print("Line 5 - Value of c is ", c)

c **= a  # c **= a is equivalent to c = c ** a
print("Line 6 - Value of c is ", c)

c //= a  # c //= a is equivalent to c = c // a
print("Line 7 - Value of c is ", c)

##  Python Bitwise Operators ##


a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b  # 12 = 0000 1100 <= Binary AND
print("Line 1 - Value of c is ", c)

c = a | b  # 61 = 0011 1101 <= Binary OR
print("Line 2 - Value of c is ", c)

c = a ^ b  # 49 = 0011 0001  <= Binary XOR
print("Line 3 - Value of c is ", c)

c = ~a  # -61 = 1100 0011 <= Binary Ones Complement
print("Line 4 - Value of c is ", c)

c = a << 2  # 240 = 1111 0000 <= Binary Left Shift
print("Line 5 - Value of c is ", c)

c = a >> 2  # 15 = 0000 1111 <= Binary Right Shift
print("Line 6 - Value of c is ", c)

## Python Logical Operators ##

x = 5

if (x > 3 and x < 10):
    print("True")  # returns True because 5 is greater than 3 AND 5 is less than 10
else:
    print("False")

print(
    x > 3 or x < 4)  # returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

print(not (x > 3 and x < 10))  # returns False because not is used to reverse the result

## Python Membership Operators ##

a = 10
b = 20
listdata = [1, 2, 3, 4, 5];

if a in listdata:
    print("Line 1 - a is available in the given list")
else:
    print("Line 1 - a is not available in the given list")

if b not in listdata:
    print("Line 2 - b is not available in the given list")
else:
    print("Line 2 - b is available in the given list")

a = 2
if a in listdata:
    print("Line 3 - a is available in the given list")
else:
    print("Line 3 - a is not available in the given list")

## Python Identity Operators ##

# Identity operators compare the memory locations of two objects.

a = 20
b = 20

if a is b:
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")

if id(a) == id(b):
    print("Line 2 - a and b have same identity")
else:
    print("Line 2 - a and b do not have same identity")

b = 30
if a is b:
    print("Line 3 - a and b have same identity")
else:
    print("Line 3 - a and b do not have same identity")

if a is not b:
    print("Line 4 - a and b do not have same identity")
else:
    print("Line 4 - a and b have same identity")

## Python Operators Precedenc ##

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("Value of (a + b) * c / d is ", e)

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("Value of ((a + b) * c) / d is ", e)

e = (a + b) * (c / d)  # (30) * (15/5)
print("Value of (a + b) * (c / d) is ", e)

e = a + (b * c) / d  # 20 + (150/5)
print("Value of a + (b * c) / d is ", e)
