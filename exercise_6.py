name_str = "Денис, Олег, Вася, Петя,Дима,Женя"
name_list = name_str.split(',')

for i in name_list:
    name_list[name_list.index(i)] = i.strip()

print(name_list)
