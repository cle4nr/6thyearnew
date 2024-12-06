#test

dic = {'John':{'Nickname':'','Weight':'72'}}
hw = list()
lhw = list()
mw = list()
ww = list()
lw = list()
fw = list()
bw = list()
flw = list()
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
    

for fighter,data in fighters_dict2.items():
    weight = data.get("Weight")
    