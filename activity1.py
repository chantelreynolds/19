
student_data = {
"id1": {"name": "Sara", "class": "v", "subject": "english, math, science"},
"id2": {"name": "David", "class": "v", "subject": "english, math, science"},
"id3": {"name": "Sara", "class": "v", "subject": "english, math, science"},                         
"id4": {"name": "Surya", "class": "v", "subject": "english, math, science"}

}

result = {}
seen_keys = []

for students_id, student_info in student_data.items():
    unique_key = (student_info["name"], student_info["class"], student_info["subject"])
   
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[students_id] = student_info

for k, v in result.items():
    print(k, ":", v)
    