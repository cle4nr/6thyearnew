my2ddic = {}
for x in range(4):
    name = input(f'Enter name {x+1}: ')
    age = int(input('Enter their age: '))
    size = float(input('Enter their shoe size UK: '))
    my2ddic[name] = {'age':age, 'size':size}
print()    
for key, value in my2ddic.items():
    print(key, *value.items())
print()    
remv = input('Enter the name of a person you would like to remove: ')
del my2ddic[remv]
print()

for key, value in my2ddic.items():
    print(key, *value.items())
