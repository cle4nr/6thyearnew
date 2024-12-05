def averagecals(calories):
    sumcal = sum(calories)
    avgcal = sum(calories) / len(calories)
    return avgcal

#|V1−V2|[(V1+V2)2]×100=? percentage difference formula
def percentdiff(v1,v2):
    return (abs(v1-v2) / ((v1+v2) / 2)) * 100
    
    
    
    
f = open('Exercise.csv', 'r') #open in read mode
head = f.readline() #removes header
nowhitespace = [] #empty list
for line in f:
    line = line.strip() #removes white space
    line = line.split(',') #turns each line into a list
    if '' not in line: #if it has all the data (no blanks)
        nowhitespace.append(line) #add the list of data to the empty list

for l in nowhitespace: #for loop amt of lists
    l = [float(x) for x in l] #list comprehension?? idk ignore for now


headers = head.split(',')
#print('  '.join(headers)) #prints header before data
        
# for x in range (len(nowhitespace)): #for each group of data loop
#      print(*nowhitespace[x],sep='	') #* removes [''] from list

data = {}
for i in range(len(nowhitespace)):
    if int(nowhitespace[i][0]) not in data:
        data[int(nowhitespace[i][0])] = [float(nowhitespace[i][3])]
    else:
        data[int(nowhitespace[i][0])].append(float(nowhitespace[i][3])) #dictionary is only taking last piece of data in file, not all
print()
print(f"{'Duration(m)':10s} {'Average Calories':10s}")
for duration in sorted(data):
    print(f"{duration:^10}{averagecals(data[duration]):10.1f}") #:.1f puts float to 1 decimal place, :10 makes it max 10 digits long(fills rest with white space)
        

        
#for types 45 and 60 show average of top 20 and bottom 20
    #compare values to eachother and get percentage difference
    
sort45 = sorted(data[45])
sort60 = sorted(data[60])

avgbot20_45 = averagecals(sort45[:20])
avgtop20_45 = averagecals(sort45[-20:])
avgbot20_60 = averagecals(sort60[:20])
avgtop20_60 = averagecals(sort60[-20:]) #wrong
print()
print()
print(f"{'Duration(m)':7s}   {'AvgTop20-Cals':7s}   {'AvgBot20-Cals':7s}   {'Overall Average':7s}")
print(f"{'45m':^8} {avgtop20_45:10.1f}  {avgbot20_45:15.1f}{averagecals(sorted(data[45])):17.1f}")  
print(f"{'60m':^8} {avgtop20_60:10.1f}  {avgbot20_60:15.1f}{averagecals(sorted(data[60])):17.1f}")
print()
print('----------------------')
print(f"Percentage difference:")
print('----------------------')
print(f"{'Duration(m)':7s}   {'Avgtop20-and-overall-average':15s}   {'Avgbot20-and-overall-average':15s}")
print(f"{'45m':^8}  	 {percentdiff(avgtop20_45,averagecals(data[45])):10.2f}%   			{percentdiff(avgbot20_45,averagecals(data[45])):10.2f}%")
print(f"{'60m':^8}  	 {percentdiff(avgtop20_60,averagecals(data[60])):10.2f}%   			{percentdiff(avgbot20_60,averagecals(data[60])):10.2f}%")
print()

choosingdur = True
while choosingdur:
    userdur = int(input('Enter a valid duration of your own session: '))
    if userdur in data:
        choosingdur = False
    else:
        print('Your duration is not valid, Try again.')
        print('Valid durations: ',end = '')
        for key in data.keys():
            print(f"{key}, ",end='')
        print('\n')
usercal = float(input('Enter the calories burnt to one decimal place: '))
print('--------------------------------------------------------------------')
print(f"{'Duration':10s} {'Your-Calories':10s}    {'Duration-Average':10s}    {'Percent-Difference'}")
print(f"{userdur:5} {usercal:14.1f}   {round(averagecals(data[userdur]),1):15}   {percentdiff(usercal,round(averagecals(data[userdur]))):17.1f}%")

        




