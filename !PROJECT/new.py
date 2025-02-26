import statistics as st
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import datetime
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials


cred = credentials.Certificate("C:/Users/19RMcClean.ACC/Desktop/test-299b9-firebase-adminsdk-73zi2-3fa7952a98.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://test-299b9-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference('/')
fighters_dict = ref.get()



def cm_to_ft_inch(cmheight):
    import math
    inches = cmheight / 2.54
    feet = inches / 12
    frac, whole = math.modf(feet)
    ftinch = frac *12
    print(f'{int(whole)} feet {round(ftinch)} inches')
  
def weightcheck(weight):
    if weight != 'n/a':
        weight = int(weight)
        if weight > 94:
            return 8
        elif weight > 84:
            return 7
        elif weight > 78:
            return 6
        elif weight > 71:
            return 5
        elif weight > 66:
            return 4
        elif weight > 62:
            return 3
        elif weight > 58:
            return 2
        else:
            return 1
        

flw=dict()
bw=dict()
fw=dict()
lw=dict()
ww=dict()
mw=dict()
lhw=dict()
hw=dict()

divisions = {'flyweight':flw,'bantamweight':bw,'featherweight':fw,'lightweight':lw,'welterweight':ww,'middleweight':mw,'lightheavyweight':lhw,'heavyweight':hw}
for fighter,data in fighters_dict.items():
    weight = data.get("weight_in_kg")
    if weight != '':
        if weightcheck(weight) == 1:
            flw[fighter]=data
        if weightcheck(weight) == 2:
            bw[fighter]=data
        if weightcheck(weight) == 3:
            fw[fighter]=data
        if weightcheck(weight) == 4:
            lw[fighter]=data
        if weightcheck(weight) == 5:
            ww[fighter]=data
        if weightcheck(weight) == 6:
            mw[fighter]=data
        if weightcheck(weight) == 7:
            lhw[fighter]=data
        if weightcheck(weight) == 8:
            hw[fighter]=data

stances_dict = dict()
stancesall = dict()

for weightclass in divisions:
    orth1, southpaw1, switch1 = 0,0,0
    for fighter,data in divisions[weightclass].items():
        for v in data:
            if data[v] == '':
                data[v] = 'n/a'
        stance = data.get("stance")
        if stance == "Orthodox":
            orth1 += 1
        elif stance == "Southpaw":
            southpaw1+= 1
        elif stance == "Switch":
            switch1 += 1
    stancesall[weightclass] = {"orthodox":orth1,"southpaw":southpaw1,"switch":switch1}
    
piestances = input('piestances (y/n):')
if piestances == 'y':
    mylabels = ['Orthodox','Southpaw','Switch']
    y = np.array([stancesall['flyweight']['orthodox'],stancesall['flyweight']['southpaw'],stancesall['flyweight']['switch']])
    plt.pie(y, labels = mylabels)
    plt.title('Flyweight stances') #only did one weight class for this analysis, but in the website you will have the option to choose any weight class(or all)
    plt.show() 

    
    
    
    
avgheight = dict()
for weightclass in divisions:
    templist=[]
    for fighter,data in divisions[weightclass].items():
        for v in data:
            if data[v] == '':
                data[v] = 'n/a'
        height = data.get("height_cm")
        if height != 'n/a':
            templist.append(height)
    meantemp = st.mean(templist)
    roundedmean = round(meantemp, 2)
    avgheight[weightclass] = roundedmean
    
heightavg = input('heightavg (y/n):')
if heightavg == 'y':
    mylabels = ['flyweight','bantamweight','featherweight','lightweight','welterweight','middleweight','lightheavyweight','heavyweight']
    y = np.array([avgheight['flyweight'],avgheight['bantamweight'],avgheight['featherweight'],avgheight['lightweight'],avgheight['welterweight'],avgheight['middleweight'],avgheight['lightheavyweight'],avgheight['heavyweight']])
    plt.bar(mylabels, y)
    plt.title('Average reach per weight class')
    plt.xlabel('Divisions')
    plt.ylabel('Reach in cm')
    plt.show()



avgreach = dict()
for weightclass in divisions:
    templist1=[]
    for fighter,data in divisions[weightclass].items():
        for v in data:
            if data[v] == '':
                data[v] = 'n/a'
        reach = data.get("reach_in_cm")
        if reach != 'n/a':
            templist1.append(reach)
    meantemp = st.mean(templist1)
    roundedmean = round(meantemp, 2)
    avgreach[weightclass] = roundedmean
    
reachavg = input('reachavg (y/n):')
if reachavg == 'y':
    mylabels = ['flyweight','bantamweight','featherweight','lightweight','welterweight','middleweight','lightheavyweight','heavyweight']
    y = np.array([avgreach['flyweight'],avgreach['bantamweight'],avgreach['featherweight'],avgreach['lightweight'],avgreach['welterweight'],avgreach['middleweight'],avgreach['lightheavyweight'],avgreach['heavyweight']])
    plt.bar(mylabels, y)
    plt.title('Average reach per weight class')
    plt.xlabel('Divisions')
    plt.ylabel('Reach in cm')
    plt.show()




flwcount=0
bwcount=0
fwcount=0
lwcount=0
wwcount=0
mwcount=0
lhwcount=0
hwcount=0


for x in divisions:
    for fighter, data in divisions[x].items():
        if x == 'flyweight':
            flwcount +=1
        if x == 'bantamweight':
            bwcount+=1
        if x == 'featherweight':
            fwcount+=1
        if x == 'lightweight':
            lwcount+=1
        if x == 'welterweight':
            wwcount+=1
        if x == 'middleweight':
            mwcount+=1
        if x == 'lightheavyweight':
            lhwcount+=1
        if x == 'heavyweight':
            hwcount+=1
            
            
countdiv = {'flyweight':flwcount,'bantamweight':bwcount,'featherweight':fwcount,'lightweight':lwcount,'welterweight':wwcount,'middleweight':mwcount,'lightheavyweight':lhwcount,'heavyweight':hwcount}
piecount = input('piecount (y/n):')
if piecount == 'y':
    mylabels = ['flyweight','bantamweight','featherweight','lightweight','welterweight','middleweight','lightheavyweight','heavyweight']
    y = np.array([countdiv['flyweight'],countdiv['bantamweight'],countdiv['featherweight'],countdiv['lightweight'],countdiv['welterweight'],countdiv['middleweight'],countdiv['lightheavyweight'],countdiv['heavyweight']])
    plt.pie(y, labels = mylabels)
    plt.title('Amount of fighters in their respective weight class')
    plt.show() 





allfighters = dict()
allfighters['Fighters'] = fighters_dict



# ref.set(allfighters,countdiv,stancesall,avgheight,avgreach) #the analytics for each weight class, aka all data that will be displayed on website e.g. amount of fighters per weight class, average height of weight classes etc
            
            
            
    
    


        

