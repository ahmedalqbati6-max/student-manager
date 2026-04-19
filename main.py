students = []

def add_student(name, age):
    students.append({"name": name, "age": age})

def view_students():
    for s in students:
        print(s["name"], s["age"])

add_student("Ahmed", 20)
add_student("Ali", 22)

view_students()
