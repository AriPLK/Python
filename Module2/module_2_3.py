my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
y = 0
while y < len(my_list):
    if my_list[y] > 0:
        print(my_list[y])
    elif my_list[y] < 0:
        break
    y += 1
