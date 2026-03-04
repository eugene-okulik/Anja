import datetime

need_time = 'Jan 15,2023 - 12:05:33'
python_date = datetime.datetime.strptime(need_time, '%b %d,%Y - %H:%M:%S')
print(python_date.strftime('%B'))
print(datetime.datetime.strftime(python_date, '%d.%m.%Y, %H:%M'))

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25,
                29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

temperatures2 = list(filter(lambda x: x > 28, temperatures))
max_temp = max(temperatures2)
average_temp = sum(temperatures2) / len(temperatures2)
min_temp = min(temperatures2)

print(f'''
жаркие дни - {temperatures2}
максимальная температура - {max_temp},
средняя температура - {round(average_temp, 3)},
минимальная температура - {min_temp}
''')
