def answer(number):
    if number < 3 or number > 20:
        return "Необходимо ввести число в диапазоне от 3 до 20"
    result = ""
    i = 1
    while i < 20:
        j = i + 1
        while j <= 20:
            if number % (i + j) == 0:
                result += f"{i}{j}"
            j += 1
        i += 1
    return result


num = int(input("Введите число от 3 до 20: "))
print(answer(num))
