# iterates over the items of any sequence (a list or a string),

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[users] = status


for i in range(1, 5):
    print(i)

else:
    print('The for loop is over')

for letter in 'Python':
    print(letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print(fruit)

print("Good Bye")

# Iterating by Sequence Index
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print(fruits[index])
print("Good Bye")

# Using else Statement with For Loop
for num in range(10, 20):
    for i in range(2, num):
        if num%i == 1:
            j = num/i
            print(num,i,j)
            break
    else:
        print(num)
