# task_2
from orca.debug import println
result = []
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        result.append("FuzzBuzz")
    elif number % 3 == 0:
        result.append("Fuzz")
    elif number % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(number))

# Выводим каждый элемент с новой строки
for item in result:
    print(item)
