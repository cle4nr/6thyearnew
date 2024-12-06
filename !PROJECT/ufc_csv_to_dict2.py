def convert_value(value):
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            pass
    return value

with open("ufc-fighters-statistics-cut2.csv") as data_file:
    headers = data_file.readline().split(",")[1:]
    
    fighters_dict = dict()
    fighters_dict2 = dict()
    
    for line in data_file:
        name, data = line.strip().split(",", maxsplit=1)
        values = list()
        for value in data.split(","):
            #print(f"{value=}")
            values.append(convert_value(value))
            #print(f"{value=}")    
        fighters_dict[name] = values
        fighters_dict2[name] = { headers[i]:values[i] for i in range(len(values)) }
        
    heights = list()
    weights = list()
    for fighter,data in fighters_dict2.items():
        heights.append(data.get("height_cm"))
        weights.append(data.get("weight_in_kg"))

import matplotlib.pyplot as plt
# plt.boxplot(heights, showmeans=True, meanline=True)
plt.grid(axis="y")
bins = [ i for i in range(165, int(max(heights))+5, 5)]
plt.hist(heights, bins, ec="black")
# plt.scatter(x=weights, y=heights)    
plt.show()
        
        