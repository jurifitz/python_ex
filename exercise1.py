##copy code into python console
name = str(input("Hello, please tell me your name "))
age = int(input("and your age"))
a = age
cntr = 0
while a % 10 != 0:
    if a % 10 != 0:
        a = a + 1
        cntr = cntr + 1
else:
    print(f"Hello {name}, now you are {age} years old. That means in {cntr} years you'll be {a}")
