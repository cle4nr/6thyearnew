# ch099
list2d = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
rowdis = int(input('Enter the row you would like displayed(1-4): '))
rowdis = rowdis - 1
print('Row',rowdis+1,':',list2d[rowdis])
column = int(input('Enter the column in that row you would like displayed(1-3): '))
column = column - 1
print('The value at this location is:',list2d[rowdis][column])
choosing = True
while choosing:
    yn = input('\nWould you like to change this value(y or n): ')
    if yn == 'y':
        choosing = False
if yn == 'y':
    newval = int(input('Enter a new value: '))
    list2d[rowdis][column] = newval
    print('Your new row:',list2d[rowdis])
    print('Your new 2d list:')
    for x in range(len(list2d)):
        print(list2d[x][0],list2d[x][1],list2d[x][2])
        