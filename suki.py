date_ = {'Sandi':1997,'Sara':2001,'Andrei':2003}
print(date_)
print(date_.get('Andrei'))
print(date_.get('Max','Ошибка ввода!'))
date_.update({'Anton':2002,
               'Dana':2004})
print(date_.pop('Sandi'))
print(date_)

my_set = {1, 2, 5, 4, 3, 2, 5, 65, 345, 76, 3, 1, 8, 5, 4}
print(my_set)
my_set.update({40,26})
my_set.remove(76)
print(my_set)