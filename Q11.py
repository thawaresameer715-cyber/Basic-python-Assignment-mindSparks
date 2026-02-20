#11. Function: Input list of tuples (id, score); sort by score descending using sorted() and loop.

def sort_scores(data):
    sorted_list = sorted(data, key=lambda x: x[1], reverse=True)
    
    for item in sorted_list:
        print(f"ID: {item[0]} | Score: {item[1]}")
    
    return sorted_list

student_data = [("A101", 85), ("B202", 92), ("C303", 78), ("D404", 95)]
sort_scores(student_data)