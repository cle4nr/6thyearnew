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


    
#		---
def getmean(llist):
    listsum = sum(llist)
    length = len(llist)
    mean = listsum / length
    return mean
print(getmean(weights))
print(getmean(heights))
# 		---







#sigstrikabsorbedandlanded,sigacc,sigdef,tdavg,tdacc,tddef,tdattempts,subavg,reach, if all == 0, remove fighter

