#ch101
my2ddic = {'John': {'N':3056,'S':8463,'E':8441,'W':2694},'Tom': {'N':4832,'S':6786,'E':4737,'W':3612},'Anne': {'N':5239,'S':4802,'E':5820,'W':1859},'Fiona': {'N':3904,'S':4802,'E':8821,'W':2451}}
cords = ['N','S','E','W']
names = ['John', 'Tom', 'Anne', 'Fiona']

for key, value in my2ddic.items():
    print(key, *value.items())

choosingname = True
while choosingname:
    name = input("Enter a sales person's name: ")
    if name in names:
        choosingname = False
    else:
        print('Name not in list.')
choosingregion = True
while choosingregion:
    region = input('Enter a region: ')
    region = region.upper()
    if region in cords:
        choosingregion = False
    else:
        print('Region must be N, S, E or W')
choosingint = True
while choosingint:
    valuenew = input('Enter a valid alteration for the sales figure: ')
    if valuenew.isdigit():
        choosingint = False
    else:
        print('Enter a valid number')


my2ddic[name][region] = valuenew

for key, value in my2ddic.items():
    print(key, *value.items())

    
