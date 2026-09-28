print("\nDICTIONARIES")

marks = {"Ava": 88, "Liam": 92, "Mia": 79}
print("Student marks:", marks)

marks["Noah"] = 85
print("After adding Noah:", marks)

del marks["Mia"]
print("After deleting Mia:", marks)

more_marks = {"Emma": 91, "Oliver": 87}
merged_marks = marks.copy()
merged_marks.update(more_marks)
print("Merged dictionaries:", merged_marks)

student_name = "Ava"
print(f"Is {student_name} in the marks dictionary?", student_name in marks)

sentence = "python is fun and python is useful"
word_counts = {}
for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print("Word frequencies:", word_counts)

top_student = max(merged_marks, key=merged_marks.get)
print("Student with the highest mark:", top_student)

original = {"one": 1, "two": 2, "three": 3}
reversed_dictionary = {value: key for key, value in original.items()}
print("Reversed dictionary:", reversed_dictionary)

marks["Ava"] = 95
print("Ava's updated mark:", marks["Ava"])

student_pairs = [("Ethan", 89), ("Sofia", 94), ("Lucas", 82)]
students = dict(student_pairs)
print("Dictionary from tuple list:", students)