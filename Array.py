courses = ["MIT", "Data Science", "Machine Learning", "Computer Science"]

print(courses)

# printing specific courses from the array using index
print(courses[0])
print(courses[1])
print(courses[2])
print()

# looping through the array to print the courses without the index and special brackets

for course in courses:
    print(course)
print()

# adding an element in an array
courses.append("Android Development")
print(courses)
print()

# removing an element from an array
courses.remove("MIT")
print(courses)