Number_1 = int(input("Enter a First number: "))
Number_2 = int(input("Enter a Second number: "))

if Number_1 > 0 and Number_2 > 0:
    print("The number1 is", Number_1, "and Number2 is", Number_2, "Both are positive")

elif Number_1 == 0 or Number_2 == 0:
    print("The number1 is", Number_1, "and Number2 is", Number_2, "One of the numbers is zero")

else:
    print("The number1 is", Number_1, "and Number2 is", Number_2, "At least one number is negative")