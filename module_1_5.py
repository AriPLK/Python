immutable_var = (1, 2, True, "string", 3.12)
print(immutable_var)
#immutable_var[1] = 2
#Объект tuple не поддерживает изменения элементов внутри него, кроме 2 исключений
#immutable_var = ([True, False], "string")
#immutable_var[0][1] = True
#immutable_var = (1, 2) * 4
mutable_var = [1, 2, True, 'string', 3.12]
mutable_var[2] = False
print(mutable_var)