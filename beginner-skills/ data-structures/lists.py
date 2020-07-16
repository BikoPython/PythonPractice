shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')

for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')

shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)


list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5];
list3 = ["a", "b", "c", "d"]

# Accessing Values in Lists
print(list1[0])
print(list2[1:5])

# Updating Lists

list1[2] = 2001;
print(list1)

# Delete List Elements

del list1[1]

len(list1)


list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5];

print(max(list2))

list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]

print(max(list1))
print(max(list2))


aTuple = (123, 'xyz', 'zara', 'abc');

list(aTuple)


aList = [123, 'xyz', 'zara', 'abc'];

aList.append(2999)
print(aList)

aList = [123, 'xyz', 'zara', 'abc', 123];
aList.count(123)
aList.count('Zara')

aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];

aList.extend(bList)

aList = [123, 'xyz', 'zara', 'abc']
aList.index('zara')

aList = [123, 'xyz', 'zara', 'abc']
aList.insert(3, 'kuja')
print(aList)

aList = [123, 'xyz', 'zara', 'abc']
aList.pop(2)

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.remove('abc')

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.reverse()
print(aList)
