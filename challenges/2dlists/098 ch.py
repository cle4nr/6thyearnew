#098 ch
list2d = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
rowdis = int(input('Enter the row you would like displayed: '))
rowdis = rowdis - 1
print(list2d[rowdis])
    
addval = int(input('Enter a value to add to this row '))
list2d[rowdis].append(addval)
print(list2d[rowdis])