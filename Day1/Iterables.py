print(type(5))
print(type(range(5)))

#Iterables are objects that can be iterated over, meaning you can loop through them. Examples of iterables include lists, tuples, strings, dictionaries, and sets. The range() function is also an iterable that generates a sequence of numbers.
for x in "python":
    print(x)

for x in range(5):
    print(x)

for x in [1, 2, 3, 4, 5]:
    print(x)

for key, value in {"name": "Rupesh", "age": 30, "city": "New York"}.items():
    print(key, ":", value)

