zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))

singleton = (2 , )

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5);
tup3 = "a", "b", "c", "d";

# Accessing Values in Tuples

print(tup1[0])
print(tup2[1:5])

# Updating Tuples
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

 # Following action is not valid for tuples
tup1[0] = 100;

# create a new tuple as follows
tup3 = tup1 + tup2;
print(tup3)

# Delete Tuple Elements
# Removing individual tuple elements is not possible.
tup = ('physics', 'chemistry', 1997, 2000);
print(tup);
del tup1



# Indexing, Slicing, and Matrixes
L = ('spam', 'zak', 'rotam');
print(L[2])
print(L[-2])
print(L[1:])
