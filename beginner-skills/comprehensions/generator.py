 # Generator comprehensions use circular brackets whereas list comprehensions use square brackets.

 # Generators don’t allocate memory for the whole list.
 # Instead, they generate each value one by one which is why they are memory efficient

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_gen = (var for var in input_list if var % 2 == 0)

print("Output values using generator comprehensions:", end = ' ')

for var in output_gen:
    print(var, end = ' ')
