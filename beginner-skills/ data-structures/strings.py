# This is a string object

name= 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))


# Accessing Values in Strings
var1 = "Python Programming"
var1[0:5]


# Updating Strings

var1 = 'Hello World!'

var1[0:6] + 'Python'
print(var1)


# String Formatting Operator

print("My name is %s and weight is %d kg!" % ('Zara', 21))
