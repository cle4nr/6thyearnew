#ch 110

f = open('names.txt','r')
print('List of all names(names.txt)\n')
names = f.readlines()
for x in range(len(names)):    
    names[x] = names[x].strip()
    print(names[x])
choosing = True
while choosing: 
    remvName = input('\nEnter one of the names in the file you would like to remove\n') #to do: add doofus after 3 fails
    if remvName in names:
        choosing = False

names.remove(remvName)
print()
f = open('names2.txt','w')
for x in names:
    f.write(x + '\n')

f.close()
f = open('names2.txt','r')
for x in f:
    print(x.strip())
    









'''f = open('C:\\Users\\19RMcClean.ACC\\Downloads\\Exercise.csv', 'r')
head = f.readline()
ld = []
l2 = []
for line in f:
    line = line.strip()
    line = line.split(',')
    if '' not in line:
        l2.append(line)

for l in l2:
    l = [float(x) for x in l]
    

        
print(head)

        
for x in range (len(l2)):
    print(*l2[x],sep='	')'''
    
    

    