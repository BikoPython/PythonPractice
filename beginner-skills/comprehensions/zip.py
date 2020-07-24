# [xv if c else yv for (c,xv,yv) in zip(condition,x,y)]

# Making two lists a list making pairs:

a = [1, 2, 3]
b = [4, 5, 6]

z = list(zip(a,b))
print(z)

# Reverse the course, and get each list back.
c, d = zip(*z)
print(c, d)

# Dictionary construction with zip
# Keys and values must be computed at runtime:

D1 = {'a': 1, 'b': 2, 'c': 3}
print(D1)

# make it by assigning values to keys::
D1 = {}
D1['a'] = 1
D1['b'] = 2
D1['c'] = 3
D1['d'] = 4
print(D1)

# Keys and values in lists at runtime:

keys = ['a', 'b', 'c']
values = [1, 2, 3]

# zip the lists and loop through them in parallel:
list(zip(keys,values))

D2 = {}

for (k,v) in zip(keys, values):
    D2[k]=v

print(D2)

# make a dict from zip result:

D3 = dict(zip(keys, values))
print(D3)


x = [1,2,3,4,5]
y = [11,12,13,14,15]
condition = [True,False,True,False,True]
[xv if c else yv for (c,xv,yv) in zip(condition,x,y)]
