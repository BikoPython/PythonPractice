

for age in range(1, 10):
    if age % 2 == 0:
        continue

    print(age)

while True:
    s = 'ke'

    if s == 'quit':
        break

    if len(s) < 3:
        print('Too small')

        continue
    print('Input is of sufficient length')
    # Do other kinds of processing here...

for letter in 'Python':
    if letter == 'h':
        continue
    print('Current Letter :', letter)

var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print('Current variable value:', var)
print("Good Bye!")
