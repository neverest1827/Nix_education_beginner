name = input('write name').strip()
lastName = input('write last name').strip()
txt = 'My name is {} and last name is {}'

print(txt.format(name.capitalize(), lastName.capitalize()))
