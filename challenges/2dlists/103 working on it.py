my2ddic = {}
for x in range(4):
    name = input(f'Enter name {x+1}: ')
    age = int(input('Enter their age: '))
    size = float(input('Enter their shoe size UK: '))
    my2ddic[name] = {'age':age, 'size':size}
    
for key, value in my2ddic.items():
    for index in value:
        if not index == 'size':
            print(key,',' value[index])