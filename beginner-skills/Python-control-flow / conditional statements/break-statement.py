for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break

    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


while True:
    s = 'quit'                #input('Enter something: ')

    if s == 'quit':
        break

    print('Length of the string is', len(s))

print('Done')


for letter in 'Python':
    if letter == 'h':
        break
    print('Current Letter:', letter)

var = 10
while var > 0:
    print('Current variable value :', var)
    var = var -1
    if var == 5:
        break
print("Good Bye!")
