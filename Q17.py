#Nested dict {class: {student: grades}}; function to find class average using recursion-like loops

school_data = {
    "Math": {
        "Alice": [90, 80, 85],
        "Bob": [70, 75, 80]
    },
    "Science": {
        "Charlie": [100, 95, 98],
        "Diana": [88, 92, 90]
    }
}

def get_class_averages(data):
    class_avg_results = {}

    for class_name, students in data.items():
        all_grades_in_class = []
        
        for student, grades in students.items():
            for grade in grades:
                all_grades_in_class.append(grade)
        
        if all_grades_in_class:
            class_avg_results[class_name] = sum(all_grades_in_class) / len(all_grades_in_class)
            
    return class_avg_results

averages = get_class_averages(school_data)

for cls, avg in averages.items():
    print(f"{cls} Class Average: {avg:.2f}")