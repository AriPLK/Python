def is_prime(func):
    def wrapper(*args):
        a = func(*args)
        is_Prime = True
        for j in range(2, a):
            if a % j == 0:
                is_Prime = False
                break
        if is_Prime:
            return f'Простое\n{func(*args)}'
        else:
            return f'Составное\n{func(*args)}'

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
