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
