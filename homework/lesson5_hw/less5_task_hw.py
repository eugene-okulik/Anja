#task_1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

#task_2
#option_1
a = 'результат операции: 42'.index('42')
b = 'результат операции: 514'.index('514')
c = 'результат работы программы: 9'.index('9')
print(
    ((int('результат операции: 42'[a:])) + 10),
    ((int('результат операции: 514'[b:])) + 10),
    ((int('результат работы программы: 9'[c:])) + 10)
)

#option_2
a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'
aid=a.index('42')
bid=b.index('514')
cid=c.index('9')
print(
    ((int(a[aid:])) + 10),
    ((int(b[bid:])) + 10),
    ((int(c[cid:])) + 10)
)

#task_3
students=['Ivanov', 'Petrov', 'Sidorov']
subjects=['math', 'biology', 'geography']
sb=','.join(subjects)
#option_1 - string-format
print('Students {0} study these subjects: {1}'.format(','.join(students), sb))

#option_2 - f-string
print(f'Students {','.join(students)} study these subjects: {sb}')