#12. Dictionary of {student: [grades]}; compute averages with loop, store in new dict, print 

student_grades = {
    "Alice": [85, 90, 92],
    "Bob": [70, 88, 75],
    "Charlie": [95, 100, 98],
    "Diana": [82, 80, 85]
}

averages = {}

for student, grades in student_grades.items():
    avg = sum(grades) / len(grades)
    averages[student] = round(avg, 2)

for student, avg in averages.items():
    print(f"Student: {student} | Average: {avg}")