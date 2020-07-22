## Assigning Values to Variables ##
counter = 100  # An integer assignment
miles = 1000.0  # A floating point
name = "John"  # A string

print(counter)
print(miles)
print(name)

##  Multiple Assignment ##

a = b = c = 1  # assign a single value to several variables simultaneously
print(a)
print(b)
print(c)
x, y, z = 1, 2, "john"  # assign multiple objects to multiple variables
print(x)
print(y)
print(z)

## Standard Data Types :Python has five standard data types − Numbers, String, List, Tuple, Dictionary ##

## Python Numbers ##

var1 = 1  # Number data types store numeric values.
var2 = 10
print(var1)
print(var2)

del var1, var2  # delete a single object or multiple objects by using the del statement.

## Python Strings ##

str = 'Hello World!'

print(str)  # Prints complete string
print(str[0])  # Prints first character of the string
print(str[2:5])  # Prints characters starting from 3rd to 5th
print(str[2:])  # Prints string starting from 3rd character
print((str + " ") * 3)  # Prints string three times
print(str + " TEST")  # Prints concatenated string

## Python Lists ##
# A list contains items separated by commas and enclosed within square brackets ([]) #
# A list can be accessed using the slice operator ([ ] and [:]) with indexes
# starting at 0 in the beginning of the list
# and working their way to end -1.
# The plus (+) sign is the list concatenation operator,
# and the asterisk (*) is the repetition operator.

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)  # Prints complete list
print(list[0])  # Prints first element of the list
print(list[1:3])  # Prints elements starting from 2nd till 3rd
print(list[2:])  # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist)  # Prints concatenated lists

## Python Tuples ##
# A tuple is another sequence data type that is similar to the list.
# Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed,
# while tuples are enclosed in parentheses ( ( ) ) and cannot be updated.
# Tuples can be thought of as read-only lists.

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)  # Prints the complete tuple
print(tuple[0])  # Prints first element of the tuple
print(tuple[1:3])  # Prints elements of the tuple starting from 2nd till 3rd
print(tuple[2:])  # Prints elements of the tuple starting from 3rd element
print(tinytuple * 2)  # Prints the contents of the tuple twice
print(tuple + tinytuple)  # Prints concatenated tuples

## Python Dictionary ##
# Python's dictionaries are kind of hash table type.
# They work like associative arrays or hashes found in Perl and consist of key-value pairs.
# A dictionary key can be almost any Python type, but are usually numbers or strings.
# Values, on the other hand, can be any arbitrary Python object.

# Dictionaries are enclosed by curly braces ({ }) and
# values can be assigned and accessed using square braces ([]).

dictvar = {}
dictvar['one'] = "This is one"
dictvar[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dictvar['one'])  # Prints value for 'one' key
print(dictvar[2])  # Prints value for 2 key
print(tinydict)  # Prints complete dictionary
print(tinydict.keys())  # Prints all the keys
print(tinydict.values())  # Prints all the values


