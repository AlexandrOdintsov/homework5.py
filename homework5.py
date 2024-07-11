immutable_var = 1, 2, 3, 4, "Hello", True
print (immutable_var)
#immutable_var [1]=25
#print (immutable_var) #'tuple' object does not support item assignment - объект "кортеж" не поддерживает назначение элементов
mutable_list = [9, 8, 7, 6, "Zero", False]
mutable_list[2]=1000
print(mutable_list)