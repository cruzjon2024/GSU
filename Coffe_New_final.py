import pandas as pd 
import numpy as np
import dateutil.parser as parser
import sys

coffee=pd.read_csv("/Users/jonathancruz/Desktop/VS Code Workspace/Data programming /Coffee Chain.csv",parse_dates=['Ddate'])

#print(coffee.dtypes)


#Data Cleaning 
coffee=coffee.drop("Number of Records", axis=1)
coffee["Ddate"].astype({'Ddate': 'datetime64[ns]'})
coffee["Budget Sales"].astype(int)
#coffee["Area Code"].astype(str)


c2 = coffee._get_numeric_data()
c2[c2 < 0] = 0


#print(c2)

def Method1(coffee):
    products=[]
    for x in coffee["Profit"]:
        for y in coffee["Product Type"]:
            if x >= 50 :
                products.append(y)
    return pd.unique(products)
        
def Method2(df):
    area_profit = {} # dict for storing profit of each area code
    for areacode in df['Area Code'].unique(): # looping through area codes
        if areacode not in area_profit.keys():
            area_profit[areacode]=df[df['Area Code'] == areacode]['Profit'].sum() # storing total profit of particular area code in key value pair
    v = list(area_profit.values()) # listing values
    k = list(area_profit.keys()) # listing keys
    return k[v.index(max(v))]
    #print("Area Code with Max profit:",k[v.index(max(v))]) # getting key (area code) with maximum value



def method4(coffee, e):
    coffee["type2"]= coffee.iloc[:,e].str.lower()
    return coffee["type2"]




def method5(df):
    #Question 5 - Produce an error if 
    qoutes=[]
    for i in df["Area Code"].unique(): 
        for cal in df["Inventory"]:
            for j in df["Budget Cogs"]:
                try:
                    qoutes.append([i,cal/j])
                except Exception as e:
                    return("Error",e)
    return pd.DataFrame(qoutes)
      
