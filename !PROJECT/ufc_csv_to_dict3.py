import numpy as np
import matplotlib.pyplot as plt
import datetime
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials


#when displaying data, only use data that != 0, lots missing


def getmean(llist):
    listsum = sum(llist)
    length = len(llist)
    mean = listsum / length
    return mean


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
        

        
        

f = open('testwrite.csv','w')
with open("ufc-fighters-statistics_all.csv") as data_file:
    headersstring = data_file.readline().strip("\n")
    headers = headersstring.split(",")[1:]
    fighters_dict = dict()
    
    for line in data_file:
        name, data = line.strip().split(",", maxsplit=1)
        values = list()
        for value in data.split(","):
            values.append(convert_value(value))
        if '.' in name:
            name = name.replace('.','')
            name = name.replace("'","")
            
        fighters_dict[name] = {headers[i]:values[i] for i in range(len(values))}
        
    heights = list()
    weights = list()
    
    
    
    orth = 0
    southpaw = 0
    switch = 0
    for fighter,data in fighters_dict.items():
        for v in data:
            if data[v] == '':
                data[v] = 'n/a'
        date_ob = data.get("date_of_birth")
        stance = data.get("stance")
        if stance == "Orthodox":
            orth += 1
        elif stance == "Southpaw":
            southpaw += 1
        elif stance == "Switch":
            switch += 1
    greenfn = input("compare 2 fighter's data?(y/n) ")
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
#             make so if data type is a digit that it compares both on bar chart

            x = [fighterin1, fighterin2]
            y = [fighter1data,fighter2data]
            plt.bar(x,y,color = ['red','blue'])
            plt.title(datanyl)
            plt.show()
        else:
            print(f"{fighterin2}, {datanyl}: {fighter2data}")
            print(f"{fighterin1}, {datanyl}: {fighter1data}")
            x = [fighterin2, fighterin1]
            y = [fighter1data, fighter2data]
            plt.bar(x,y,color = ['red','blue'])
            plt.title(datanyl)
            plt.show()
            
    stances_dict = {"orthodox":orth,"southpaw":southpaw,"switch":switch}
    piein = input('Stances Pie-chart(show): ')
    if piein == 'show':
        stances_dict = {"orthodox":orth,"southpaw":southpaw,"switch":switch}
        plt.pie(stances_dict.values(),labels=stances_dict.keys(),autopct="%1.2f%%")
        explode = (0,0.2,0)
        plt.show()
        
        
    flw=dict()
    bw=dict()
    fw=dict()
    lw=dict()
    ww=dict()
    mw=dict()
    lhw=dict()
    hw=dict()

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
    hwmean = getmean(hwheightlist)
    lhwheightlist = list()
    for fighter,data in lhw.items():
        lhwheight = data.get('height_cm')
        if lhwheight != '':
            lhwheightlist.append(lhwheight)
    lhwmean = getmean(lhwheightlist)
    mwheightlist = list()
    for fighter,data in mw.items():
        mwheight = data.get('height_cm')
        if mwheight != '':
            mwheightlist.append(mwheight)
    mwmean = getmean(mwheightlist)
    wwheightlist = list()
    for fighter,data in ww.items():
        wwheight = data.get('height_cm')
        if wwheight != '':
            wwheightlist.append(wwheight)
    wwmean = getmean(wwheightlist)
    lwheightlist = list()
    for fighter,data in lw.items():
        lwheight = data.get('height_cm')
        if lwheight != '':
            lwheightlist.append(lwheight)
    lwmean = getmean(lwheightlist)
    fwheightlist = list()
    for fighter,data in fw.items():
        fwheight = data.get('height_cm')
        if fwheight != '':
            fwheightlist.append(fwheight)
    fwmean = getmean(fwheightlist)
    bwheightlist = list()
    for fighter,data in bw.items():
        bwheight = data.get('height_cm')
        if bwheight != '':
            bwheightlist.append(bwheight)
    bwmean = getmean(bwheightlist)
    flwheightlist = list()
    for fighter,data in flw.items():
        flwheight = data.get('height_cm')
        if flwheight != '':
            flwheightlist.append(flwheight)
    flwmean = getmean(flwheightlist)

    
        
        

# ref.set(fighters_dict)
        