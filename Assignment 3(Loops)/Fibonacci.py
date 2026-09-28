n = 10

a = 0
b = 1
result = []

for i in range(n):
    result.append(a)
    a, b = b, a + b

print(result)