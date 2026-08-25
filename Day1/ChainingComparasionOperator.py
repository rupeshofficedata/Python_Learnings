age = int(input("Enter your age: "))
#if age >= 18 and age < 65:
if 18 <= age < 65: # Chaining comparison operators
    print("Eligible for work.")
else:
    print("Not eligible for work.")