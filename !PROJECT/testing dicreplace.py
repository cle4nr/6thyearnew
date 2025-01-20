# testing
def dicreplacecomma(dic):
    for fighter,data in dic.items():
        for item in data:
            if '.' in item:
                item = item.replace('.',',')
dict1 = {'fighter':{'height': 170.2, 'weight':82.5}}
dicreplacecomma(dict1)
print(dict1)