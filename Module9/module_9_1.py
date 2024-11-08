def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        a = func(int_list)
        update_result = {func.__name__: a}
        result.update(update_result)
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))