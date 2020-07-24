 # Python deque uses the opposite rule, LIFO queue, or last in first out.Operate on stacks and queues.


# deque is a container class in Python which can hold a collection of python objects.

# Add to left:                            Add to right:
# extendleft()                            extend()
# appendleft()                            append()
#
# Remove from left:                       Remove from right:
# popleft()                               pop()

from collections import deque
import collections

#Create an empty deque
d1 = collections.deque()

#add few elements to the right side of the deque
d1.append(10)
d1.append(10.1)
d1.append("abc")

print("Contents of the deque")
print(d1)

# Creation of a deque from an iterable object:

# A tuple of prime numbers
primeNumbers = (3, 5, 7)

#creating a deque from an already existing iterable object - in this case a tuple

primeDeque = collections.deque(primeNumbers)
print("Initial deque")
print(primeDeque)
primeDeque.append(11)
primeDeque.append(13)
primeDeque.append(13)
primeDeque.appendleft(2)
print("Deck after append and appendleft:")
print(primeDeque)


# Creation of a deque from an iterable object:

# creating a fixed size deque
dequeInstance = collections.deque(maxlen=5)

# add 5 elements to the right side

dequeInstance.append(10)
dequeInstance.append(20)
dequeInstance.append(30)
dequeInstance.append(40)
dequeInstance.append(50)

print(dequeInstance)

# add 1 element to the right side

dequeInstance.append(60)
print(dequeInstance)

# add 1 element to the left side

dequeInstance.appendleft(5)
print(dequeInstance)


base = deque([1, 2, 3])
base.rotate()
print(base)

base1 = deque([1, 2, 3, 4, 5])

# rotates base 2 steps to the left
base1.rotate(-2)
print(base1)

# rotates base 3 steps to the right
base1.rotate(3)
print(base1)


waitlist = deque()

waitlist.append('Erin')
waitlist.append('Samantha')
waitlist.append('Joe')
waitlist.append('Martin')
waitlist.append('Helena')

print(waitlist)

# Removed the first item in our list
waitlist.popleft()
print(waitlist)


# Remove all of the items in our deque,
deque.clear()
print(waitlist)


# you can initialize a deque with a list
numbers = deque()

# Use append like before to add elements
numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)

# You can pop like a stack
last_item = numbers.pop()
print(last_item)
print(numbers)
