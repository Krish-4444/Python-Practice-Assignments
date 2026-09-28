number = 123
result = 0

while number > 0:
    digit = number % 10
    result = result + digit
    number //= 10

print("Reversed Number:", result)