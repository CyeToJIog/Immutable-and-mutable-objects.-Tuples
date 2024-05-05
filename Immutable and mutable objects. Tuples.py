
immutable_var = ("food",1,True)
mutable_list = ["people",2024,False]
print(immutable_var)
# immutable_var [0] = "apple" # кортеж нельзя изменить т.к он не изменяем
#print(immutable_var)
print(mutable_list)
mutable_list[0] = "human"
mutable_list[1] = 2025
mutable_list[2] = True
print(mutable_list)
