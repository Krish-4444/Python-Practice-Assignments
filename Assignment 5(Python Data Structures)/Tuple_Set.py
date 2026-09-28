print("TUPLES")

numbers = (10, 20, 30, 40, 50)
print("Numbers:", numbers)

print("Third number:", numbers[2])

first, second, third, fourth, fifth = numbers
print("Unpacked:", first, second, third, fourth, fifth)


print("\nSETS")

fruits = {"apple", "banana", "orange", "grape", "mango"}
print("Fruits:", sorted(fruits))

fruits.add("pineapple")
print("After adding pineapple:", sorted(fruits))

fruits.discard("grape")
print("After removing grape:", sorted(fruits))

first_set = {1, 2, 3, 4}
second_set = {3, 4, 5, 6}
print("Union:", sorted(first_set.union(second_set)))

print("Intersection:", sorted(first_set.intersection(second_set)))

small_set = {1, 2}
large_set = {1, 2, 3, 4}
print("Is small_set a subset of large_set?", small_set.issubset(large_set))

values = [1, 2, 2, 3, 3, 3, 4]
unique_values = set(values)
print("Unique values:", sorted(unique_values))

