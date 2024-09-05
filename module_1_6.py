my_dict = {'John': 2000, 'Kiri': 1995, 'Misha': 1996}
print(my_dict)
my_dict['John'] = 2001
my_dict['Mira'] = 1998
print(my_dict)
my_dict.update({'Ivan': 1985,
                'Sofia': 2003})
del(my_dict['Sofia'])
print(my_dict)


my_set = {1, 2, 3, True, 'Name', 3.14, 3, True, False}
print(my_set)
my_set.update({5, 9})
my_set.discard(False)
print(my_set)
