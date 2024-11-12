first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(x) - len(y) for x, y in list(zip(first, second)) if len(x) != len(y)]
second_result = [len(x) == len(y) for x in first for y in second if first.index(x) == second.index(y)]

print(list(first_result))
print(list(second_result))
