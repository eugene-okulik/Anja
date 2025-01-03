my_dict = {
    'tuple': ('t1', 't2', 't3', 't4', 't5'),
    'list': ['l1', 'l2', 'l3', 'l4', 'l5'],
    'dict': {'key_1': 'd1', 'key_2': 'd2',
             'key_3': ' d3', 'key_4': 'd4', 'key_5': 'd5'},
    'set': {'s1', 's2', 's3', 's4', 's5'}
}

print(my_dict['tuple'][-1])

my_dict['list'].append('l6')
my_dict['list'].pop(1)

my_dict['dict']['i am tuple'] = 'anything'
del my_dict['dict']['key_1']

my_dict['set'].add('s6')
my_dict['set'].remove('s2')

print(my_dict)
