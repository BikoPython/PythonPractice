# Offers a continuous storage container for homogenous types.
import array


# Create an array of integers using the type code 'i'
intArray = array.array('i')

# Insert elements into the Python array
for i in range(10, 0, -1):
    intArray.insert(0, i);
print("Contents of the array:");
print(intArray);

print("Address and length of the array:");
print(intArray.buffer_info());

print("Size of an element in the array:");
print(intArray.itemsize);

print("The total memory occupied by the array:");
print(intArray.buffer_info()[1]*intArray.itemsize);
