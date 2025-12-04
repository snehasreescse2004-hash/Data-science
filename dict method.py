student = {"name": "diya", "age": 21, "city": "chennai"}
print(student)

print(student.get("name"))

print(student.keys())

print(student.values())

print(student.items())

student.update({"age":"22"})
print(student)

student.pop("age")
print(student)

student.clear()
print(student)

student = {"name": "sneha", "age": 21}
new_student = student.copy()
print(new_student)

student = {"name": "sneha"}
student.setdefault("age", 21)
print(student)

    