def convert_value(value):
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            pass
    return value
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
    
    fighters_dict2 = dict()
    
    for line in data_file:
        name, data = line.strip().split(",", maxsplit=1)
        values = list()
        for value in data.split(","):
            values.append(convert_value(value))
        fighters_dict2[name] = { headers[i]:values[i] for i in range(len(values)) }
        
    heights = list()
    weights = list()
    
    hwdict = dict()

    for fighter,data in fighters_dict2.items():
        height = data.get("height_cm")
        if height:
            heights.append(height)
        weight = data.get("weight_in_kg")
        if weight:
            weights.append(weight)
        
        
        
def getmean(llist):
    listsum = sum(llist)
    length = len(llist)
    mean = listsum / length
    return mean

print(getmean(weights))
print(getmean(heights))

import matplotlib.pyplot as plt
plt.boxplot(heights, showmeans=True, meanline=True)
plt.grid(axis="y")
# bins = [ i for i in range(165, int(max(heights))+5, 5)]
# plt.hist(heights, bins, ec="black")
# bins = [ i for i in range(150, int(max(weights))+5, 10)]
# plt.hist(weights, bins, ec="black")
# plt.scatter(x=weights, y=heights)    

        
        