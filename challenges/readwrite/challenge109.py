#109


list123 = [1,2,3]
choosing = True
while choosing:
    numin = int(input('1) Create a new file\n2) Display the file\n3) Append new item to the file and display\nMake a selection 1, 2, or 3\n'))  
    if numin in list123:
        choosing = False
    
if numin == 1:
    subject = input('Enter a school subject\n')
    f = open('Subjects.txt','w')
    f.write(subject)
    f.close()
if numin == 2:
    f = open('Subjects.txt','r')
    print('Subjects.txt\n')
    print(f.read())
if numin == 3:
    newsub = input('Enter a new school subject to append to the file\n')
    print('\n')
    f = open('Subjects.txt','a')
    f.write('\n')
    f.write(newsub)
    f = open('Subjects.txt','r')
    print(f.read())

    
    
