my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
y = 0
while y < len(my_list):
    for nums in my_list:
        if nums > 0:
            print(nums)
        elif nums < 0:
            break
        y += 1


