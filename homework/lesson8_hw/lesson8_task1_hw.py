import random

salary = int(input('What is your salary? '))
bonus = random.choice([True, False])
amount_bonus = random.randint(100, 1000)

if bonus:
    result_salary = salary + amount_bonus
else:
    result_salary = salary
print(f"{salary}, {bonus} - '${result_salary}'")
