#112ch
f = open('Books.csv','r')
header = f.readline()
print(header)
for line in f:
    print(line,end='')
print()


a = open('Books.csv','a')
name = input('Input name of book: ')
author = input('Input name of author: ')
year = input('Input year released: ')

name = name + ', '
author = author + ', '

a.write('\n')
newline = [name,author,year]
for x in newline:
    a.write(x)    
a.close()
    

f = open('Books.csv','r')
header = f.readline()
print(header)
for line in f:
    print(line,end='')