list_student =[]
list_courses = []
list_mark = []
n = int(input("Number of students: "))
m = int(input("Number of courses:"))
if (n < 0 or m < 0):
    print("Invalid")
    exit()
for i in range(n):
    sid = int(input("Enter student id: "))
    name = input("Enter student name: ")
    dob = input("Enter date of birth: ")
    list_student.append({
        "id": sid,
        "name": name,
        "DOB" : dob
    })

for i in range(m):
    id = int(input("Enter course id: "))
    name_courses = input("Enter name of the course: ")  
    list_courses.append({
        "id": id,
        "name": name_courses
    })
print("Courses available: ")
for course in list_courses:
    print(f"{course['id']}: {course['name']}")
course_id = int(input("Enter course id: "))

for student in list_student:
    mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
    if mark <0 or mark > 20:
        print("invalid")
        exit()
    list_mark.append({
        "student_id": student['id'],
        "course_id": course_id,
        "mark": mark
    })

course_id_show = int(input("Enter course id to display marks: "))

print(f"Marks for course ID {course_id_show}:")
for entry in list_mark:
    if entry["course_id"] == course_id_show:
       student_name = ""
    for s in list_student:
            if s["id"] == entry["student_id"]:
                student_name = s["name"]
                break 
    print(f"{student_name} (ID: {entry['student_id']}): {entry['mark']}")

