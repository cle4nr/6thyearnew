l = [9,2,4,7,5]
e = []
sml = 0
n = (len(l))
for x in range(n):
    sml = 0 #this resets before running next pass
    for i in range(n):
        if l[sml] > l[i]: 
            sml = i
            l.remove(l[sml])
            e.append(l[sml]) #need to find out how to remove sml from previous list before finding next smallest
            
        
            

        
print(l)
print(e)
        
    
    
    
    