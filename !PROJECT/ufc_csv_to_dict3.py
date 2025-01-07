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
    
with open("ufc-fighters-statistics_all.csv") as data_file:
    headers = data_file.readline().split(",")[1:]
    
    fighters_dict = dict()
    
    for line in data_file:
        name, data = line.strip().split(",", maxsplit=1)
        values = list()
        for value in data.split(","):
            values.append(convert_value(value))
        fighters_dict[name] = { headers[i]:values[i] for i in range(len(values)) }
        
    heights = list()
    weights = list()
    
    orth = 0
    southpaw = 0
    switch = 0
    for fighter,data in fighters_dict.items():
        height = data.get("height_cm")
        if height:
            heights.append(height)
        weight = data.get("weight_in_kg")
        if weight:
            weights.append(weight)
        stance = data.get("stance")
        if stance == "Orthodox":
            orth += 1
        elif stance == "Southpaw":
            southpaw += 1
        elif stance == "Switch":
            switch += 1
        else: pass
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
        weight = float(weight)
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
    hworthlist = list()
    for fighter,data in hw.items():
        hwheight = data.get('height_cm')
        if hwheight != '':
            hwheight = int(hwheight)
            hwheightlist.append(hwheight)
        
        
# --- most wins ---        
#     highwin = 0    
#     for fighter,data in fighters_dict.items():
#         wins = data.get("wins")
#         
#         if wins >= highwin:
#             highwin = wins
#             
#     for fighter,data in fighters_dict.items():
#         wins = data.get("wins")
#         if wins==253:
#             print(fighter,data)

# --- most losses ---        
#     highloss = 0    
#     for fighter,data in fighters_dict.items():
#         losses = data.get("losses")
#         
#         if losses >= highloss:
#             highloss = losses
#           
#             
#     for fighter,data in fighters_dict.items():
#         losses = data.get("losses")
#         if losses == 83:
#             print(fighter,data)

    
        
def getmean(llist):
    listsum = sum(llist)
    length = len(llist)
    mean = listsum / length
    return mean

# print(getmean(weights))
# print(getmean(heights))

# <<<<<<< Updated upstream
stances_dict = {"orthodox":orth,"southpaw":southpaw,"switch":switch}
# =======
# import matplotlib.pyplot as plt

# plt.hist(heights, bins, ec="black")
# bins = [ i for i in range(150, int(max(weights))+5, 10)]
# plt.hist(weights, bins, ec="black")
# plt.scatter(x=weights, y=heights)    
# >>>>>>> Stashed changes


# plt.boxplot(hwheightlist, showmeans=True, meanline=True)
# plt.grid(axis="y")
# bins = [ i for i in range(165, int(max(heights))+5, 5)]

# --- stances pie chart ---
# import numpy as np
# import matplotlib.pyplot as plt
# plt.pie(stances_dict.values(),labels=stances_dict.keys())
# plt.show()

            
        