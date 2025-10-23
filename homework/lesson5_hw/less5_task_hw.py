'''homework_5'''
#task_1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

#task_2
a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'

ind_a = a.index(':')
ind_b = b.index(':')
ind_c = c.index(':')

int_a = int(a[ind_a + 1:].strip())
int_b = int(b[ind_b + 1:].strip())
int_c = int(c[ind_c + 1:].strip())

print(int_a + 10, int_b + 10, int_c + 10)

#task_3
students=['Ivanov', 'Petrov', 'Sidorov']
subjects=['math', 'biology', 'geography']
sb=','.join(subjects)
print(f'Students {','.join(students)} study these subjects: {sb}')
