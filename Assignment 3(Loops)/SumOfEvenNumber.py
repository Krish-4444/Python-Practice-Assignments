number = 100
result = 0

for i in range(1, number + 1):
    if(i %2 == 0):
        result += i

print("Sum of even numbers from 1 to", number, "is", result)