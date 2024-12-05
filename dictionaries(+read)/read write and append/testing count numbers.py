f = open('numbers.csv','r')
header = f.readline()
whole = []
for line in f:
    line = line.strip()
    line = line.split(', ')
    for v in line:
        v = int(v)
        whole.append(v)

val = int(input('Enter a value to count in file:	'))
if whole.count(val) > 0:
    print(whole.count(130))
else:
    print('value not in file')
