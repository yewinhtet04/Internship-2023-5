import json

# a Python object (dict):
x = {
    "name": ["John", 'baby'],
    "age": 30,
    "city": {'hometown': "New York", 'work': 'London'}
}
print('KEYS',x.keys())
# CLEAR
cityTemperature = {"New York": 18, "Texas": 26}

print("Dictionary before clear():", cityTemperature)

# removes all the items from the dictionary
cityTemperature.clear()

print("Dictionary after clear():", cityTemperature)

# COPY
original = {1: 'one', 2: 'two'}
new = original

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)

original = {1: 'one', 2: 'two'}
new = original.copy()

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)

# FROMKEYS
# keys for the dictionary
alphabets = {'a', 'b', 'c'}

# value for the dictionary
number = 1

# creates a dictionary with keys and values
dictionary = dict.fromkeys(alphabets, number)

print(dictionary)

# Output: {'a': 1, 'c': 1, 'b': 1}

alphabets.clear()
print('CLEAR ORIGINAL',dictionary)

# list of numbers
keys = [1, 2, 4]

# creates a dictionary with keys only
numbers = dict.fromkeys(keys)

print(numbers)

# set of vowels
keys = {'a', 'e', 'i', 'o', 'u'}

# list of number
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)

# updates the list value
value.append(2)

print(vowels)

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]

# creates dictionary using dictionary comprehension
vowels = {key: list(value) for key in keys}

print(vowels)

# updates the value list
value.append(2)

print(vowels)

#GET
person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))

print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))


# value is provided
print('Salary: ', person.get('salary', 0.0))

person = {}

# Using get() results in None
print('Salary: ', person.get('salary'))


# Using [] results in KeyError
#print(person['salary'])

#ITEMS
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

items = sales.items()

print('Original items:', items)

# delete an item from dictionary
del[sales['apple']]

print('Updated items:', items)

#KEYS
employee = {'name': 'Phill', 'age': 22}

# extracts the dictionary keys
dictionaryKeys = employee.keys()

print('Before dictionary update:', dictionaryKeys)

# adds an element to the dictionary
employee.update({'salary': 3500.0})

# prints the updated view object
print('After dictionary update:', dictionaryKeys)

#POP
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('apple')

print('The popped element is:', element)
print('The dictionary is:', sales)

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('guava', 'banana')

print('The popped element is:', element)
print('The dictionary is:', sales)

#POPITEMS
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

# ('salary', 3500.0) is inserted at the last, so it is removed.
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)

# inserting a new element pair
person['profession'] = 'Plumber'

# now ('profession', 'Plumber') is the latest element
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)

person = {'name': 'Phill'}

#SETDEFAULT
# key is not in the dictionary
salary = person.setdefault('name','hh')
print('person = ',person)
print('12334356salary = ',salary)

# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = ',person)
print('age = ',age)

#UPDATE
d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)

print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)

print(d)

dictionary = {'x': 2}

dictionary.update([('y', 3), ('z', 0)])

print(dictionary)

#VALUES
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

values = sales.values()

print('Original items:', values)

# delete an item from dictionary
del[sales['apple']]

print('Updated items:', values)