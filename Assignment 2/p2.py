Number_1= int(input("Enter a number: "))

if Number_1 <= 0:
    print("The Given number is" , Number_1 ,"Zero or negative number not allowed.")
elif Number_1 % 2 == 0:
    print("The Given number is" , Number_1 ,"is even.")
else:
    print("The Given number is" , Number_1 ,"is odd.")

