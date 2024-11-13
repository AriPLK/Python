def all_variants(text):
    for char in text:
        yield char

    for i in range(len(text) - 1):
        yield text[i] + text[i+1]

    yield text



a = all_variants("abc")
for i in a:
    print(i)