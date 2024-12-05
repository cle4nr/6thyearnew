import pandas as pd

df = pd.read_csv('unclean_data1.csv')
#or overwrite encoding
#df = pd.read_csv('unclean_data.csv',encoding='ANSI'
#print(df)

#df.columns = df.columns.str.upper()
#df.columns = df.columns.str.lower()
#print(df.columns)

'''
df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})
#Case sensitive 'DURATION' is not the same as 'duration'
df = df.rename(columns = { {'DURATION':'TIME'})
print(df.columns)
'''