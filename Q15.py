#15. Function to remove duplicates from list of dicts by key 'id' using set of ids.

def unique_by_id(data_list):
    seen_ids = set()
    unique_list = []
    
    for item in data_list:
        if item['id'] not in seen_ids:
            unique_list.append(item)
            seen_ids.add(item['id'])
            
    return unique_list

raw_data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"},
    {"id": 3, "name": "Charlie"}
]

clean_data = unique_by_id(raw_data)
print(clean_data)