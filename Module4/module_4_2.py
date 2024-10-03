def test_function(*args):
    def inner_function(*args):
        print('Я в области видимости функции test_function')

    inner_function()

test_function()

try:
    inner_function() #При вызове этой функции вне test_function программа выводит ошибку
except:
    print('Функция вне области видимости')