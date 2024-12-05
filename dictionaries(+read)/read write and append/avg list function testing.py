#avg of list
calories = [700.0,563.2,604.1,500.0,500.0,500.4,500.3,466.4]

def averagecals(calories):
    sumcal = sum(calories)
    avgcal = sum(calories) / len(calories)
    return avgcal
print(averagecals(calories))
check = []
for x in range(3): 
    fltcheck = float(input())
    check.append(fltcheck)
print(averagecals(check))