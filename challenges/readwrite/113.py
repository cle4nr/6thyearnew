#112ch
f = open('Books.csv','r')
header = f.readline()
print(header)
for line in f:
    print(line,end='')
print()
howmany = int(input('How many records do you want to add to the list: '))
a = open('Books.csv','a')
for x in range(howmany):
    newline = []
    
    name = (input('Input name of book: '))
    author = (input('Input name of author: '))
    year = (input('Input year released: '))
    name = name + ', '
    author = author + ', '
    newline.append(name)
    newline.append(author)
    newline.append(year)
    a.write('\n')
    for x in newline:
        a.write(x)
a.close()

f = open('Books.csv','r')
authors = []
for line in f:
    line = line.split(', ')
    if not line[1] in authors:
        authors.append(line[1])
choosing = True
while choosing:
    authorname = input('Enter name of an author to display book(s): ')
    if authorname in authors:
        choosing = False
    if not authorname in authors:
        print("Author's name not in list, try again")
f = open('Books.csv','r')    
for line in f:
    line = line.split(', ')
    if line[1] == authorname:
        print(line[0])
        
    
    
    