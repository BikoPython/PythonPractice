
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

count = 0
while (count < 9):
    print(count)
    count = count + 1

print("Good Bye!")

# The Infinite Loop
var = 1
while var == 1:
    num = 20
    print("You entered: ", num)

print("Good Bye!")


# Using else Statement with While Loop
count = 0
while count < 5:
    print(count, "is less than 5")
    count = count + 1
else:
    print(count, "is not less than 5")

flag = 1
while(flag):print("Given flag is really true!")
print("Good Bye!")
