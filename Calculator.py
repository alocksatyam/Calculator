
print("~~~~~~ Mini Calculator ~~~~~~")

num1 = float(input("Enter Number Here: "))
num2 = float(input("Enter Number Here: "))

print("""
press 1 for addition
press 2 for subtraction
press 3 for multiplication
press 4 for division""")

choice = int(input("Enter a number between 1 - 4: "))

if choice == 1:
    sum = num1 + num2
    print("The addition of given two numbers is:", sum)

elif choice == 2:
    subtraction = num1 - num2
    print("The subtraction of given two numbers is:", subtraction)

elif choice == 3:
    multiplication = num1 * num2
    print("The multiplication of given two numbers is:", multiplication)

elif choice == 4:
    division = num1 / num2
    print("The division of given two numbers is:", division)



else:
    print("Invalid input","\nPlease check the option you choose")