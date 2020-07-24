# Similar to the syntax for dictionary comprehensions. The only difference is that
# sets just have values instead of key:value pairs.
# create an output set which contains only the even numbers that are present in the input list.

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
output_set = set()


# Using loop for constructing output set
for var in input_list:
    if var % 2 == 0:
        output_set.add(var)
print("Output Set using for loop:", output_set)


# Using Set comprehensions for constructing output set
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
set_using_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:", set_using_comp)

# Given the list:
names = ['Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]

set = { name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }
print(set)


 # dictionary in which the occurrences of upper and lower case characters are combined:

mcase = {'a':10, 'b': 34, 'A': 7, 'Z':3}
mcase_frequency = {k.lower() : mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()}
print(mcase_frequency)

{s for s in [1,2,1,0]}

{s**2 for s in [1,2,1,0]}

{s**2 for s in range(10)}

{s for s in [1,2,3] if s%2}

{(m,n) for n in range(2) for m in range(3, 5)}

# Construct a list of integers which are not prime (which are the product of two integers)
no_primes = {a * multiplier for multiplier in range(2, 100) for a in range(2, 100)}

# Since 1 is not a prime number we have to add it to this list
no_primes.add(1)

# Now construct a list of primes out of this list
primes = {p for p in range(1, 100) if p not in no_primes}
print(primes)

a_set = set(range(10))
print(a_set)

{x ** 2 for x in a_set}

{x for x in a_set if x % 2 == 0}

{2**x for x in range(10)}

# Set Comprehension:
import random
from random import randint

seed = 1234
random.seed(seed)
x = 0
y = 5
a = [randint(x, y) for i in range(0, 10)]
print(a)

random.seed(seed)
x = 0
y = 5
b = {randint(x, y) for i in range(0, 10)}
print(b)

random.seed(seed)
a = ['Even' if i % 2 == 0 else 'Odd' for i in range(10)]
print(a)

random.seed(seed)
b = {'Even' if i % 2 == 0 else 'Odd' for i in range(10)}
print(b)
