## Python IF Statement ##
# The if statement contains a logical expression using which data is compared and
# a decision is made based on the result of the comparison.

var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)

var2 = 0
if var2:
    print("2 - Got a true expression value")
    print(var2)
print("Good bye!")

## Python IF...ELIF...ELSE Statements ##

# An else statement can be combined with an if statement. An else statement contains the block of code
# that executes if the conditional expression in the if statement resolves to 0 or a FALSE value.

var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)
else:
    print("1 - Got a false expression value")
    print(var1)

var2 = 0
if var2:
    print("2 - Got a true expression value")
    print(var2)
else:
    print("2 - Got a false expression value")
    print(var2)

print("Good bye!")

# The elif statement allows you to check multiple expressions for TRUE and
# execute a block of code as soon as one of the conditions evaluates to TRUE.

var = 100
if var == 200:
    print("1 - Got a true expression value")
    print(var)
elif var == 150:
    print("2 - Got a true expression value")
    print(var)
elif var == 100:
    print("3 - Got a true expression value")
    print(var)
else:
    print("4 - Got a false expression value")
    print(var)

print("Good bye!")

## Python nested IF statements ##

# In a nested if construct, you can have an if...elif...else
# construct inside another if...elif...else construct.

var = 100
if var < 200:
    print("Expression value is less than 200")
    if var == 150:
        print("Which is 150")
    elif var == 100:
        print("Which is 100")
    elif var == 50:
        print("Which is 50")
    elif var < 50:
        print("Expression value is less than 50")
else:
    print("Could not find true expression")

print("Good bye!")

## Single Statement Suites ##

var = 100
if var == 100: print("Value of expression is 100")
print("Good bye!")


