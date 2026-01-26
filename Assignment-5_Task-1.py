student_marks = {
    "Prince": 85,
    "Raj": 78,
    "Mahi": 92,
    "Priyansh": 88
}

search_name = input("Enter the student's name: ")

if search_name in student_marks:
    print(f"{search_name}'s marks: {student_marks[search_name]}")
else:
    print("Student not found,Please enter a valid name.")