import statistics as st
import numpy as np
import matplotlib.pyplot as plt
import datetime
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials


ref = db.reference('/')
fighters_dict = ref.get()


#when displaying data, only use data that != 0, lots missing
#make a mean function of list


def getage(dob):
    if dob == 'n/a':
        return 'not recorded'
    else:
        year,month,day = map(int,dob.split('-'))
        today = datetime.date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))
        return age
    
    
def dicreplacecomma(dic):
    for fighter,data in dic.items():
        for item in data:
            item = item.replace('.',',')
 

def convert_value(value):
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            pass
    return value

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
        

for fighter,data in fighters_dict.items():
    for v in data:
        if data[v] == '':
            data[v] = 'n/a'
    date_ob = data.get("date_of_birth")
greenfn = input("compare 2 fighter's data?(y/n) ") #make it not case sensitive
if greenfn == 'y':
    fighterin1 = input("enter a fighter's name: ")
    fighterin2 = input("enter a different fighter's name: ")
    print()
    print(fighterin1,fighters_dict[fighterin1])
    print()
    print(fighterin2,fighters_dict[fighterin2])
    print()
    datanyl = input('enter a valid data point to compare: ')
    
    fighter1data = fighters_dict[fighterin1].get(datanyl)
    fighter2data = fighters_dict[fighterin2].get(datanyl)
    print()
    if datanyl == 'date_of_birth':
        if getage(fighter1data) >= getage(fighter2data):
            print(f"{fighterin1} is older.")
            print(f"{fighterin1}, {datanyl}: {fighter1data}")
            print(f"{fighterin2}, {datanyl}: {fighter2data}")
        else:
            print(f"{fighterin2} is older.")
            print(f"{fighterin2}, {datanyl}: {fighter2data}")
            print(f"{fighterin1}, {datanyl}: {fighter1data}")
            
    
    elif fighter1data >= fighter2data:
        print(f"{fighterin1}, {datanyl}: {fighter1data}")
        print(f"{fighterin2}, {datanyl}: {fighter2data}")

        x = [fighterin1, fighterin2]
        y = [fighter1data,fighter2data]
        plt.bar(x,y,color = ['red','blue']) #make it so it only print graph if data is a number
        plt.title(datanyl)
        plt.show()
    else:
        print(f"{fighterin2}, {datanyl}: {fighter2data}")
        print(f"{fighterin1}, {datanyl}: {fighter1data}")
        x = [fighterin2, fighterin1]
        y = [fighter2data, fighter1data]
        plt.bar(x,y,color = ['red','blue'])
        plt.title(datanyl)
        plt.show()
print()
    
weights=list()
heights=list()

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
        weights.append(weight)
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

        
hwheightlist = list()
for fighter,data in hw.items():
    hwheight = data.get('height_cm')
    if hwheight != '':
        hwheightlist.append(hwheight)

lhwheightlist = list()
for fighter,data in lhw.items():
    lhwheight = data.get('height_cm')
    if lhwheight != '':
        lhwheightlist.append(lhwheight)

mwheightlist = list()
for fighter,data in mw.items():
    mwheight = data.get('height_cm')
    if mwheight != '':
        mwheightlist.append(mwheight)

wwheightlist = list()
for fighter,data in ww.items():
    wwheight = data.get('height_cm')
    if wwheight != '':
        wwheightlist.append(wwheight)

lwheightlist = list()
for fighter,data in lw.items():
    lwheight = data.get('height_cm')
    if lwheight != '':
        lwheightlist.append(lwheight)

fwheightlist = list()
for fighter,data in fw.items():
    fwheight = data.get('height_cm')
    if fwheight != '':
        fwheightlist.append(fwheight)

bwheightlist = list()
for fighter,data in bw.items():
    bwheight = data.get('height_cm')
    if bwheight != '':
        bwheightlist.append(bwheight)

flwheightlist = list()
for fighter,data in flw.items():
    flwheight = data.get('height_cm')
    if flwheight != '':
        flwheightlist.append(flwheight)


whichdiv = input('enter a division to get stance pie chart(flyweight, bantamweight, etc or all): ')  
if whichdiv in divisions:
    orth1, southpaw1, switch1 = 0,0,0
    for fighter,data in divisions[whichdiv].items():
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
    stances_dict = {"orthodox":orth1,"southpaw":southpaw1,"switch":switch1}
    plt.pie(stances_dict.values(),labels=stances_dict.keys(),autopct="%1.2f%%")
    plt.title(f'Stances {whichdiv}')
    plt.show()
elif whichdiv == 'all':
    orth1, southpaw1, switch1 = 0,0,0
    for fighter,data in fighters_dict.items():
        for v in data:
            if data[v] == '':
                data[v] = 'n/a'
        stance = data.get("stance")
        if stance == "Orthodox":
            orth1 += 1
        elif stance == "Southpaw":
            southpaw1 += 1
        elif stance == "Switch":
            switch1 += 1

    stances_dict = {"orthodox":orth1,"southpaw":southpaw1,"switch":switch1}
    plt.pie(stances_dict.values(),labels=stances_dict.keys(),autopct="%1.2f%%")
    plt.title('Stances All Weight Classes')
    plt.show()
        
print()

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
greenfn2 = input("compare 2 division's amount of fighters?(y/n) ") 
if greenfn2 == 'y':
    whichdiv1 = input('enter a division to compare(flyweight, bantamweight, etc): ')  
    whichdiv2 = input('enter a second division: ')
    print()
    if whichdiv1 and whichdiv2 in divisions:
        x = [whichdiv1, whichdiv2]
        y = [countdiv[whichdiv1],countdiv[whichdiv2]]
        plt.bar(x,y,color = ['purple','yellow'])
        plt.title('Amount of Fighters')
        plt.show()
print() 
greenfn3 = input("compare 2 division's data?(y/n) ") 
if greenfn3 == 'y':
    whichdiv1 = input('enter a division to compare(flyweight, bantamweight, etc): ')  
    whichdiv2 = input('enter a second division: ')
    div1 = {}
    div2 = {}
    div1_1 = {}
    div2_1 = {}
    div2_2 = []
    div1_2 = []
    if whichdiv1 and whichdiv2 in divisions:
        datanyl1 = input('enter a data type to compare: ')
        for fighter,data in divisions[whichdiv1].items():
            if datanyl1 in data:
                datanyl2 = data.get(datanyl1)
                if datanyl2 != 'n/a' and datanyl2:
                    div1[fighter] = datanyl2
                    div1_1[fighter]=data
                    div1_2.append(datanyl2)
        
        for fighter,data in divisions[whichdiv2].items():
            if datanyl1 in data:
                datanyl2 = data.get(datanyl1)
                if datanyl2 != 'n/a' and datanyl2:
                    div2[fighter] = datanyl2
                    div2_1[fighter]=data
                    div2_2.append(datanyl2)

    x = [whichdiv1,whichdiv2]
    y = [st.mean(div1_2),st.mean(div2_2)]
    plt.bar(x,y,color = ['green','blue'])
    plt.title(datanyl1)
    plt.show()

#make another dictionary of all fighters or decide if it should be included at all
#ref.set() the analytics for each weight class, aka all data that will be displayed on website e.g. amount of fighters per weight class, average height of weight classes etc
            
            
            
    
    


        