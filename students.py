grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_ = sorted(students)
avr_grades = []
for grades_ in grades:
    total = sum(grades_)
    count = len(grades_)
    average = total / count
    avr_grades.append(average)

keys = students_
values = avr_grades
students_grades = dict(zip(keys, values))
print(students_grades)
