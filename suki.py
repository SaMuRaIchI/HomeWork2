immutable_var = 1,2,4,'clovo'       #Значение элемента кортежа можно изменить тольео если он в []
print(immutable_var)                                       #В других случаях он не изменяем
mutable_list = [1,2],3,'clovo'
print(mutable_list)
mutable_list[0][1] = 'samka'
mutable_list[0][0] = 4
print(mutable_list)