f = open('dic.csv','r')
dic = {}
for line in f:
    line = line.strip('\n')
    line = line.split(', ')
    dic[line[0]] = line[1]
print(dic)