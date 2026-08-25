# Function that perfroms a task and returns None
def greet1(name):
    print(f"Hello 1, {name}!")
    
# Function that returns a value    
def get_rounded_value(value):
    return round(value)

# Function that returns None
def greet(name):
    return f"Hello 2, {name}!"

print(greet1("Alice")) #prints Hello 1, Alice! and None
print(get_rounded_value(3.7)) #prints 4
print(greet("Bob")) #prints Hello 2, Bob!