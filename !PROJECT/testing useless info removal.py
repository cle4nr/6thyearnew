fighters_dict = {'Adam Torres':{'nickname': 'n/a', 'wins': 4, 'losses': 3, 'draws': 0, 'height_cm': 177.8, 'weight_in_kg': 77.11, 'reach_in_cm': 'n/a', 'stance': 'n/a', 'date_of_birth': 'n/a', 'significant_strikes_landed_per_minute': 0, 'significant_striking_accuracy': 0, 'significant_strikes_absorbed_per_minute': 0, 'significant_strike_defence': 0, 'average_takedowns_landed_per_15_minutes': 0, 'takedown_accuracy': 0, 'takedown_defense': 0, 'average_submissions_attempted_per_15_minutes': 0},
       'Gerald Strebendt': {'nickname': 'The Finishing Machine', 'wins': 9, 'losses': 7, 'draws': 0, 'height_cm': 175.26, 'weight_in_kg': 70.31, 'reach_in_cm': 'n/a', 'stance': 'Orthodox', 'date_of_birth': '1979-03-01', 'significant_strikes_landed_per_minute': 0, 'significant_striking_accuracy': 0, 'significant_strikes_absorbed_per_minute': 4, 'significant_strike_defence': 38, 'average_takedowns_landed_per_15_minutes': 0, 'takedown_accuracy': 0, 'takedown_defense': 0, 'average_submissions_attempted_per_15_minutes': 16.4}}
def useless(dic):
    for fighter,data in dic.items():
        append = True
        reach = data.get('reach_in_cm')
        if reach == 'n/a':
            reachpresent = False
        
        sigpermin = data.get('significant_strikes_landed_per_minute')
        if sigpermin == 0:
            sigperminpresent = False
        
        stance = data.get('stance')
        if stance == 'n/a':
            stancepresent = False
            
        dob = data.get('date_of_birth')
        if dob == 'n/a':
            dobpresent = False
            
        sigacc = data.get('significant_striking_accuracy')
        if sigacc == 0:
            sigaccpresent = False
        
        sigabs = data.get('significant_strikes_absorbed_per_minute')
        if sigabs == 0:
            sigabspresent = False
        
        sigdef = data.get('significant_strike_defence')
        if sigdef == 0:
            sigdefpresent = False
        
        if reachpresent and sigperminpresent and stancepresent and dobpresent and sigabspresent and sigdefpresent == False:
            present = False
        
useless(fighters_dict)