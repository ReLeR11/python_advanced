number_of_students = int(input())

students = {}

for student in range(number_of_students):
    name, grade = input().split()

    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    print(f"{name} -> {' '.join([f'{el:.2f}' for el in grades])} (avg: {average_grade:.2f})")
