#quick sort
l = [1,8,4,9,3,5,7]
lss = []
grt = []
piv = l[-1]


for i in range(len(l)):
    if piv > l[i]:
        lss.append(l[i])
    else: grt.append(l[i])
    
print(lss)
print(grt)