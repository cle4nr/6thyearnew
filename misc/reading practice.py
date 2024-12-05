f = open('my words for file read.txt','r')

f.readline()
#for line in f:
#    print(line,end='')
sentences = []
for line in f:
    line = line.split()
    sentences.append(line)
biglist = []
for w in sentences:
    biglist.extend(w)
for x in biglist:
    print(x, end = ' ')
print('\n----------------------')
    
#print(sorted(biglist))
choosing = True
while choosing:
    srch = input('enter a word to count\n')
    if srch in biglist:
        choosing = False
        if biglist.count(srch) == 1:
            print(f"Word appears {biglist.count(srch)} time")
        else:
            print(f"Word appears {biglist.count(srch)} times")
    else: print('word not in file')

i = 0
positions = []
for w in biglist:
    i += 1
    if w == srch:
        positions.append(i)
print(f'{srch} is at index {positions} in the file')
    
#numbers count
    
    