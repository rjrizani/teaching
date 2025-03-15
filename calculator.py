print("Hello, i am simple calculator")
number1 = int(input("Please enter the value of number1: "))
number2 = int(input("Please enter the value of number2: "))
print("What would you like to do with {} and {}".format(number1, number2))
print("for addition press 1")
print("for subtraction press 2")
print("for division press 3")

option = input()
add = number1 + number2
subtract = number1 - number2
divide = number1/number2

if option == "1":
    print(add)
elif option =="2":
    print(subtract)
elif option == "3":
    print(divide)
else:
    print("Please select valid input")

