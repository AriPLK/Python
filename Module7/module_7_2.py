def custom_write(file_name, strings):
    string_position = {}
    name = file_name
    counter = 1
    for items in strings:
        file = open(name, 'a', encoding='utf-8')
        file2 = open(name, 'r', encoding='utf-8')
        position_1 = int(file.tell())
        file.write(items + '\n')
        file.close()
        file2.close()
        string_position.update({f'{counter}, {position_1}': items})
        counter += 1
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
