# 1)
# You are given a dictionary containing student names as keys and lists of their grades as values. 
# Your task is to create a summary report that calculates the average grade for each student, 
# assigns a letter grade, and determines the class average.

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

#Calculate the average grade for each student and store the results in a new dictionary called student_averages.

student_averages = {}

for student, grade in student_grades.items():
    if grade:
        avg = sum(grade) / len(grade)
        rounded_avg = round(avg, 2)
        student_averages[student] = rounded_avg
    else:
        student_averages[student] = None
        
print(student_averages)
pass
# Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, 
# and store the results in a dictionary called student_letter_grades:
student_letter_grades = {}

for student, avg in student_averages.items():
    if avg >=90:
        grade = "A"
    elif avg >= 80 <= 89:
        grade = "B"
    elif avg >= 70 <= 79:
        grade = "C"    
    elif avg >= 60 <= 69:
        grade = "D"
    else:
        grade = "F"
    student_letter_grades[student] = grade

print(student_letter_grades)

# Calculate the class average (the average of all students’ averages) and print it.

total_average = sum(student_averages.values())
class_size = len(student_averages)
class_average = total_average / class_size

print(class_average)

# Print the name of each student, their average grade, and their letter grade.

# max_name_length = max(len(name) for name in student_grades.keys())

# for name in student_grades.keys():
#     spaces = ' ' * (max_name_length - len(name))
#     print(f"{name}:{spaces} Average Grade = {student_averages[name]:.2f}, Letter Grade = {student_letter_grades[name]}")

# Print easily the above

for name in student_grades.keys():
    average = student_averages[name]
    letter = student_letter_grades[name]

print(f"Student Name: {name}; Student Average: {average}; Student Grade: {letter}.")