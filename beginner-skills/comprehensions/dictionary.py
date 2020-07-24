# output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}
# dict_variable = {key:value for (key,value) in dictonary.items()}

 # Create an output dictionary which contains only the odd numbers that are present in the input list as keys
 # and their cubes as values.

input_list = [1, 2, 3, 4, 5, 6, 7]

output_dict = {}

# Using loop for constructing output dictionary
for var in input_list:
    if var % 2 != 0:
        output_dict[var] = var**3

print("Output Dictionary using for loop:", output_dict)


# Using Dictionary comprehensions for constructing output dictionary

input_list = [1, 2, 3, 4, 5, 6, 7]
dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:", dict_using_comp)


# construct a dictionary which maps the states with their respective capitals.
state = ['central', 'western', 'coast']
capital = ['thika', 'kakamega', 'mombasa']

output_dict = {}

# Using loop for constructing output dictionary
for (key, value) in zip(state, capital):
    output_dict[key] = value
print("Output Dictionary using for loop:", output_dict)


# Using Dictionary comprehensions for constructing output dictionary
state = ['central', 'western', 'coast']
capital = ['thika', 'kakamega', 'mombasa']

dict_using_comp = {key:value for (key, value) in zip(state, capital)}
print("Output Dictionary using dictionary comprehensions:", dict_using_comp)

t = "Apoorva"
dict = {x:t[x] for x in range(len(t))}
print(dict)

# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

# dict comprehension
myDict = { k:v for (k, v) in zip(keys, values)}
print(myDict)

sDict = {x.upper(): x*3 for x in 'coding'}
print(sDict)

# Code  using if.Maps the numbers to their cubes that are not divisible by 4:
newDict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newDict)


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Put all keys of `dict1` in a list and returns the list
dict1.keys()

# Put all values saved in `dict1` in a list and returns the list
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict1.values()


# Access each key-value pair
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict1.items()

# Dictionary comprehension
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)

#Change the names of the key.
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict1_keys = {k*2:v for (k,v) in dict1.items()}
print(dict1_keys)

# Create a new dictionary where the key is a number divisible by 2 in a range of 0-10
# and it's value is the square of the number.

numbers = range(10)
new_dict_for = {}

# Add values to `new_dict` using for loop
for n in numbers:
    if n%2 == 0:
        new_dict_for[n] = n**2

print(new_dict_for)

# Use dictionary comprehension

new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}
print(new_dict_comp)

# Alternative to lambda functions
# Used in combination with the functions filter(), map() and reduce().

# lambda function along with the map() function:
# Initialize `fahrenheit` dictionary
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

#Get the corresponding `celsius` values:
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

#Create the `celsius` dictionary:
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)

# Using dictionary comprehension:
# Initialize the `fahrenheit` dictionary:
fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}

# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
print(celsius_dict)


# If Condition:
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Check for items greater than 2
dict1_cond = {k:v for (k,v) in dict1.items() if v>2}

print(dict1_cond)

# Multiple If Conditions
dict1_doubleCond = {k:v for (k,v) in dict1.items() if v > 2 if v%2 == 0}
print(dict1_doubleCond)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
dict1_tripleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0 if v%3 == 0}
print(dict1_tripleCond)


# In a for loop, this will correspond to:
dict1dict1_tripleCond = {}

for (k,v) in dict1.items():
    if (v >= 2 and v%2 == 0 and v%3 ==0):
        dict1dict1_tripleCond[k] = v

print(dict1_tripleCond)

# If-Else Conditions:
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Identify odd and even entries:
dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}

print(dict1_tripleCond)
