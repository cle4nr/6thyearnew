f = open('names.txt')
for line in f:
    line = line.strip('\n')
    print(line)