x = int()
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('Single')
else:
    print('More')


x = 4
if x < 0:
    print("x is negative")

elif x % 2:
    print("x is positive and odd")
else:
    print("x is even and non-negative")


number = 23
guess =  50               #int(input('Enter an integer: 50'))

if guess == number:

    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')

    if True:
        print('Yes, it is true')

elif guess < number:
    print('No, it is a little higher than that')

else:
    print('No, it is a little lower than that')

print('Done')


x = 42
if x < 0:
    x = 0
    print('Negative changed to zero')

elif x == 0:
    print('Zero')

elif x == 1:
    print('Single')
else:
    print('More')
