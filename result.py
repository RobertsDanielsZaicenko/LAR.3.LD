import pandas as pd
import openpyxl

fails1 = 'description.xlsx'
fails2 = 'data.csv'
lapa = 'LookupAREA'

df1 = pd.read_excel(fails1, sheet_name=lapa)
df2 = pd.read_csv(fails2, header=0)

vieta = input()

df1['Area'] = df1['Area'].astype(str)
df2['Area'] = df2['Area'].astype(str)
df1['Description'] = df1['Description'].str.strip()

kods = df1[df1['Description'] == vieta]
atbilde = kods.iloc[0]['Area']

kods2 = df2[df2['Area'] == atbilde]
summa = kods2['geo_count'].sum()
print(summa)