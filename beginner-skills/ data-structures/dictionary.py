ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# Deleting a key-value pair
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])


# Accessing Values in Dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict['Name'])
print(dict['Age'])

# Updating Dictionary

dict['Age'] = 120;
dict['School'] = 'DPS School';


# Delete Dictionary Elements

del dict['Name'];           # remove entry with key 'Name'
dict.clear()                # remove all entries in dict
del dict;                   # delete entire dictionary
