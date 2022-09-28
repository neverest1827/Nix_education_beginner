import random

my_list = []
while len(my_list) < 100:
    my_list.append(random.randint(0, 1000))

i = 0
while i < 100:
    if my_list[i] == 777:
        print('"777" found \\(O_O)/')
        break
    elif i == 99:
        print('I dont find "777" (T_T)')
        break
    i += 1
