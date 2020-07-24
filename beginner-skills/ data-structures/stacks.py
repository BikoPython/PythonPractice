from collections import deque
# Stacks, like the name suggests, follow the Last-in-First-Out (LIFO) principle.
# As if stacking coins one on top of the other, the last coin we put on the top is
# the one that is the first to be removed from the stack later.

letters = []

# Let's push some letters into our list

letters.append('c')
letters.append('a')
letters.append('t')
letters.append('g')


# Now let's pop letters, we should get 'g'
last_item = letters.pop()
print(last_item)

# 'c' and 'a' remain
print(letters)


# Using collections.deque to Create a Python Stack
myStack = deque()

myStack.append('a')
myStack.append('b')
myStack.append('c')

myStack

myStack.pop()

myStack.pop()

myStack.pop()
