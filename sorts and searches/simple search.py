lisT = []
targ = (input("Enter target number: "))

play = True
while play == True:
    
    num2 = (input("Enter next number for your list: "))
    if "*" not in num2: #allows user to stop list when finished, without adding the stop command to the list
        lisT.append(num2)
    else: break
    
for i in range(len(lisT)):
    if lisT[i] == targ:
        print("Target number at position",i+1,"(index",i,")")
        
        
        