#ch111
f = open('Books.csv','r')
header = f.readline()
print(header)
for line in f:
    print(line,end='')
    
    
