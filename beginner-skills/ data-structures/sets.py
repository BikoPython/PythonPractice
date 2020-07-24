# Sets are unordered.
# Set elements are unique. Duplicate elements are not allowed.
# A set itself may be modified, but the elements contained in the set must be of an immutable type.

# You can define a set with the built-in set() function:

x = set(<iter>)

x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
print(x)

y = set(('foo', 'bar', 'baz', 'foo', 'qux'))
print(y)

z = set()
print(type(z),z)

s = 'data focused python'
print(s)

for c in s:
    print(c)

print(list(s))
print(set(s))

x = { 'foo', 'bar', 'baz', 'foo', 'qux' }

print(type(x), x)


x = {42, 'foo', 3.14159, None}
print(x)

# set elements must be immutable. For example, a tuple may be included in a set:

y = {42, 'foo', (1,2,3,),3.1548}
print(y)


# lists and dictionaries are mutable, so they can’t be set elements:
a = [1,2,3]
x = {a}


# Set Size and Membership:
x = {'foo', 'bar', 'baz'}
len(x)

'bar' in x

'qux' in x

# Operating on a Set
# using set union:

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

union_x = x1 | x2
print(union_x)

# note : there aren't any duplicates:
print(len(union_x), len(x1), len(x2))

# Set union can also be obtained with the .union() method:

x1.union(x2)


# Available Operators and Methods:
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print(x1.union(x2))
print(x1 | x2)


a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

print(a.union(b, c, d))
print(a | b | c | d)

# INTERSECTION

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print(x1.intersection(x2))
print(x1 & x2)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

print(a.intersection(b, c, d))
print(a & b & c & d)

# DIFFERENCE
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'quz', 'quux'}

print(x1.difference(x2))
print(x1 - x2)

a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}

print(a.difference(b, c))
print(a - b - c)

# SYMMETRIC DIFFERENCE

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print(x1.symmetric_difference(x2))
print(x1 ^ x2)

a = {1, 2, 3, 4, 5}
b = {10, 2, 3, 4, 50}
c = {1, 50, 100}

print(a ^ b ^ c)

# DISJOINT

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1.isdisjoint(x2))

x3 = x2 - {'baz'}
print(x1.isdisjoint(x3))

# IS SUBSET
x1 = {'foo', 'bar', 'baz'}
print(x1.issubset({'foo', 'bar', 'baz', 'qux', 'quux'}))

x2 = {'baz', 'qux', 'quux'}
print(x1 <= x2)

# IS PROPER SUBSET
# A set x1 is considered a proper subset of another set x2 if every element of x1 is in x2,
# and x1 and x2 are not equal.
x1 = {'foo', 'bar'}
x2 = {'foo', 'bar', 'baz'}

print(x1 < x2)

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz'}

print(x1 < x2)

# IS SUPERSET
# A set x1 is considered a superset of another set x2 if x1 contains every element of x2

x1 = {'foo', 'bar', 'baz'}
print(x1.issuperset({'foo', 'bar'}))

x2 = {'baz', 'qux', 'quux'}
print(x1 >= x2)

# IS PROPER SUPERSET
# A set x1 is considered a proper superset of another set x2 if x1 contains every element of x2,
# and x1 and x2 are not equal.
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar'}

print(x1 > x2)

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz'}

print(x1 > x2)

# Frozen Sets:
# Exactly like a set, except that a frozenset is immutable. You can perform non-modifying
# operations on a frozenset:

x = frozenset(['foo', 'bar', 'baz'])
print(x)
print(len(x))

print(x & {'baz', 'qux', 'quux'})








bri = set(['brazil', 'russia', 'india'])

'india' in bri

 'usa' in  bri

 bric = bri.copy()
 bric.add('china')
 bric.issuperset(bri)
 bri.remove('russia')
 bri & bric
