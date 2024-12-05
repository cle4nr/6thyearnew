def bubble_sort(lisT):
    n = len(lisT)
    for pass_ in range(n-1):
        for b_sort in range(n-1):
            if lisT[b_sort] > lisT[b_sort+1]: 
                placehold = lisT[b_sort]
                lisT[b_sort] = lisT[b_sort+1]
                lisT[b_sort+1] = placehold
    return(lisT)

lis1 = [5,6,7,8,9]
print(bubble_sort(lis1))
target = 7
low = 0
high = len(lis1) -1
mid = (low + high) // 2
for i in range(len(lis1)):   
    if lis1[mid] == target:
        print(lis1[mid])
        #this code does not work
    elif lis1[mid] < target:
        mid == mid + 1
    elif lis1[mid] > target:
        mid == mid - 1



