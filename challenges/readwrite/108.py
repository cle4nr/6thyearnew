newname = input('add a new name to the list:	') #asks for new name and stores
newfile = open('names.txt', 'a') #opens in append mode
newfile.write('\n')
newfile.write(newname) #writes new name in file
newfile.close() #close file to write properly

f = open('names.txt') #opens file in read mode
for line in f:  #for loop for each word
    line = line.strip('\n') #removes \n and puts all on same line
    print(line) #prints the line
    
newfile = open('names.txt','w')
newfile.write('john\nsean\nmichael\njittleyang\namelia') #it resets back to normal for testing
newfile.close() 