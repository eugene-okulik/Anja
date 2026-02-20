def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

indices = {5, 200, 1000, 100000}
results = {}

for i, value in enumerate(fibonacci(), start=1):
    if i in indices:
        results[i] = value
        if len(results) == len(indices):
            break

for i in sorted(indices):
    try:
        len_num = len(str(results[i]))
    except ValueError:
        print(f'{i}-e число Фибонначчи больше лимита Python')
        continue
    if len_num < 40:
        print(results[i])
    elif len_num <= 300:
        print(f'{len_num}-значное число')
    