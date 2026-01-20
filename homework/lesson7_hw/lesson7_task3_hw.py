def extract_number(line):
    return int(line.split(': ')[1])


lines = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for line in lines:
    print(extract_number(line) + 10)
