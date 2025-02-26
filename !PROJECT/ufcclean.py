import numpy as np
import matplotlib.pyplot as plt
import datetime
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate("C:/Users/ronan/OneDrive/Documents/GitHub/6thyearnew/!PROJECT/test-299b9-firebase-adminsdk-73zi2-3fa7952a98.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://test-299b9-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference('/')

#when displaying data, only use data that != 0, lots missing

def convert_value(value):
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            pass
    return value


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
        
    for fighter,data in fighters_dict.items():
        for v in data:
            if data[v] == '':
                data[v] = 'n/a'

ref.set(fighters_dict)
        