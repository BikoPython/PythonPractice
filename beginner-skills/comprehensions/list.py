# output_list = [output_exp for var in input_list if (var satisfies this condition)]

 # create an output list which contains only the even numbers which are present in the input list.

 # Constructing output list WITHOUT Using List comprehensions

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_list = []

 # Using loop for constructing output list

for var in input_list:
    if var % 2 == 0:
        output_list.append(var)
print("Output List using for loop:", output_list)

# Using List comprehensions for constructing output list

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

list_using_comp = [var for var in input_list if var % 2 == 0]
print("Output List using list comprehensions:", list_using_comp)


# create an output list which contains squares of all the numbers from 1 to 9.

# Constructing output list using for loop
output_list = []
for var in range(1, 10):
    output_list.append(var ** 2)
print("Output List using for loop:", output_list)


# Constructing output list using list comprehension
list_using_comp = [var**2 for var in range(1, 10)]
print("Output List using list comprehension:", list_using_comp)

# Say we need to obtain a list of all the integers in a sequence and then square them:

a_list = [1, '4', 9, 'a', 0, 4]

squared_ints = [e**2 for e in a_list if type(e) == types.IntType ]

print(squared_ints)

# The filter function applies a predicate to a sequence:
filter(lambda e: type(e) == types.IntType, a_list)

# Map modifies each member of a sequence:
map(lambda e: e**2, a_list)

# The two can be combined:

map(lambda e: e**2, filter(lambda e: type(e) == types.IntType, a_list))


# A two-level list comprehension using os.walk()
import os
restFiles = [os.path.join(d[0], f) for d in os.walk(".")
                for f in d[2] if f.endswith(".rst")]
for r in restFiles:
    print(r)


x = [i for i in range(15)]
print(x)

# create a list using “for” clause in list comprehension.
cubes = [x**3 for x in range(7)]
print(cubes)

list1 = [3, 4, 5]
new_multiplied_list = [item*2 for item in list1]
print(new_multiplied_list)

# Create a new list containing the first letters of every element in an already existing list.

listOfWords = ["this","is","python","tutorial","from","intellipaat"]
new_list = [ word[0] for word in listOfWords ]
print(new_list)

# separate the letters of a word and create a list containing
# The code block for the same in case of using for loop will be:
letters = []
for letter in 'intellipaat':
    letters.append(letter)
print(letters)

# Result using List Comprehension
letters = []
letters = [letter for letter in 'intellipaat']
print(letters)


# Lambda functions are usually used with various built-in functions such as map() filter(),
# and reduce() to work on lists.

# Map() with Lambda Function

letters = list(map(lambda x: x, 'intellipaat'))
print(letters

# List comprehension code:
New_list = [x for x in 'intellipaat']
print(New_list)

# Filter() with Lambda Function
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = list(map(int, list1))
new_list = filter(lambda x: x%2, list1)
print(list(new_list))

# Same result can be obtained using Python List Comprehension
list1 = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
print(list1)
new_list = [ x for x in list1 if x%2 ]
print(new_list)


# Reduce() with Lambda Function
from functools import reduce

list1 = [ 1, 2, 3, 4, 5, 6]
new_list = reduce(lambda x,y: x+y, list1)
print(new_list)

# List comprehensions only work with one variable,
list1 = [1,2,3,4,5,6]
new_list = sum([x for x in list1])
print(new_list)

# Conditionals in Python List Comprehension

 # Using if statement
 new_list = [x for x in range(20) if x%2 == 0]
 print(new_list)


# Using if else statement
even_odd = [f"{x} is even" if x%2==0 else f"{x} is odd" for x in range(10)]
print(even_odd)
