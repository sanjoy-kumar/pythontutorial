## Python - Loops ##

# A loop statement allows us to execute a statement or group of statements multiple times.

## While Loop ##

# A while loop statement in Python programming language repeatedly executes a target statement
# as long as a given condition is true.
from pip._vendor.distlib.compat import raw_input

count = 0
while count < 9:
    print('The count is:', count)
    count = count + 1

print("Good bye!")

## Using else Statement with While Loop ##

# If the else statement is used with a while loop,
# the else statement is executed when the condition becomes false.

count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")

## for Loop  ##

# It has the ability to iterate over the items of any sequence, such as a list or a string.

for letter in 'Python':  # First Example
    print('Current Letter :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # Second Example
    print('Current fruit :', fruit)

print("Good bye!")

## Iterating by Sequence Index ##

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('Current fruit :', fruits[index])

print("Good bye!")

## Using else Statement with For Loop ##

for num in range(10, 20):  # to iterate between 10 to 20
    for i in range(2, num):  # to iterate on the factors of the number
        if num % i == 0:  # to determine the first factor
            j = num / i  # to calculate the second factor
            print('%d equals %d * %d' % (num, i, j))
            break  # to move to the next number, the #first FOR
    else:  # else part of the loop
        print(num, 'is a prime number')
        break

## nested loops ##

# loop nesting is that you can put any type of loop inside of any other type of loop.

i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j): break
        j = j + 1
    if j > i / j: print(i, " is prime")
    i = i + 1

print("Good bye!")

## The Infinite while Loop ##

# A loop becomes infinite loop if a condition never becomes FALSE.
var = 1
while var == 1:  # This constructs an infinite loop
    num = raw_input("Enter a number  :")
    print("You entered: ", num)  # you need to use CTRL+C to exit the program.

print("Good bye!")
