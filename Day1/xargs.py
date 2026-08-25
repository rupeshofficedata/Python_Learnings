def multiply(*numbers): # syntax: def function_name(*args):
    print("Numbers to multiply:", numbers) # syntax: print(*args)
    result = 1
    for number in numbers:
        result *= number
        print(f"Multiplying {number}, current result: {result}")
    return result
    
multiply(2, 3, 4) # syntax: function_name(arguments)