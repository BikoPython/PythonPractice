
count = 0
x = 5

while x > 0:

    x = x // 2
    count += 1
print ("The approximate log2 is", count)

number = 23
running = True

while running:
    guess = 23             #int(input('Enter an integer: 50'))

    if guess == number:
        print('Congratulations, you guessed it.')
        ## this causes the while loop to stop

        running = False

    elif guess < number:
        print('No, it is a little higher than that.')

    else:
        print('No, it is a little lower than that.')

else:
    print('The while loop is over.')

print('Done')
