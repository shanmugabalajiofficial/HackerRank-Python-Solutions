#Nested Lists


students = {}

for _ in range(int(input())):
    name = input()
    grade = float(input())
    students.setdefault(grade, []).append(name)

second_lowest_grade = sorted(students.keys())[1]

print(*sorted(students[second_lowest_grade]), sep='\n')
