from math import inf
def fake_math(first, second):
    if second == 0:
        return "Ошибка"
    return first / second

def true_math(first, second):
    if second == 0:
        return inf
    return first / second