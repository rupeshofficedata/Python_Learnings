""" age = 22
if age >= 18:
    msg = "You are an adult."
else:
    msg = "You are a minor."
print(msg) """

age = int(input("Enter your age: "))
message = "You are an adult." if age >= 18 else "You are a minor."
print(message)