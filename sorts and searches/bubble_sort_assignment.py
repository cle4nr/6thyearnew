import colorama

def bubble_sort(lisT):
    n = len(lisT)
    for pass_ in range(n-1):
        for b_sort in range(n-1):
            if lisT[b_sort] > lisT[b_sort+1]: 
                placehold = lisT[b_sort]
                lisT[b_sort] = lisT[b_sort+1]
                lisT[b_sort+1] = placehold
                
                
    return(lisT)



lisT = []
play = True
while play == True:
    num1 = (input("Enter next number for your list: "))
    if "*" not in num1: #allows user to stop list when finished, without adding the stop command to the list
        lisT.append(num1)
    else: break
                 

print(colorama.Fore.GREEN + str(bubble_sort(lisT)))
                
            
            
