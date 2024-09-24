def conv_tuple(data):
    if isinstance(data, tuple):
        data = list(data)
    return data

def conv_set(data):
    if isinstance(data, set):
        data = list(data)
    return data

def counter(data):
    total = 0
    for i in data:
        if isinstance(i, int):
            total += i
        elif isinstance(i, str):
            total += len(i)
        elif isinstance(i, (tuple, list, set)):
            total += counter_all(i)
    return total

def count_dict(data):
    val_sum = 0
    if isinstance(data, dict):
        for key, value in data.items():
            val_sum += len(key)
            if isinstance(value, (int, float)):
                val_sum += value
            elif isinstance(value, (list, tuple, set, dict)):
                val_sum += counter_all([value])
    return val_sum

def counter_all(data):
    count_all = 0
    for a in data:
        if isinstance(a, int):
            count_all += a
        elif isinstance(a, str):
            count_all += len(a)

        if isinstance(a, list):
            count_all += counter(a)
        elif isinstance(a, dict):
            count_all += count_dict(a)
        elif isinstance(a, tuple):
            conv1 = conv_tuple(a)
            count_all += counter_all(conv1)
        elif isinstance(a, set):
            conv2 = conv_set(a)
            count_all += counter_all(conv2)
    return count_all

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', (('Urban2', 35)))}])
]

a = counter_all(data_structure)
print(a)
