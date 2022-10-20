
import matplotlib as mpl
import matplotlib.pyplot as plt
print('Matplotlib version:', mpl.__version__)

# 1st example 
#plt.plot(5,5, "o")

#plt.title("Sample graph")
#plt.ylabel("Sample y")
#plt.xlabel("Sample x")
#plt.text(5.01,5, "Sample annotation")
## plt.show()


#Exploring Datsets w/ pandas
import pandas as pd # primary data structure 
import numpy as np  # scinetific computing 
# reading Dataset 
df_c = pd.read_excel("Data Visualization /Canada.xlsx",
     sheet_name = 'Canada by Citizenship',
    skiprows= range(20),
    skipfooter= 2)

print(df_c)
## show column names
print(df_c.columns)

print(df_c.index)
# size of data
print(df_c.shape)

## cleaning dataset (### axis = 0 represents Rows, axis= 1 represents columns , default none = 0)
df_c.drop(['Type','Coverage', 'AREA','REG', 'DEV'], axis= 1 , inplace=True) 

print(df_c.head())

# rename the columns 
df_c.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName' : 'Region'}, inplace=True)

print(df_c.head(5))

# add a 'Total' column
df_c ['Total']= df_c.sum(axis=1)

print(df_c.head(5))
# statistical information 
print(df_c.describe())

# slicing Dataset

print(df_c.Country)
# filtering columns 
df_c[['Country', 1980,1981,1982,1983,1984]]

# how to change index. 
# To rest , use df_c.reset_index()
df_c.set_index('Country', inplace=True )

print(df_c.head(5))

## to locate specifc country name 
print(df_c.loc['Japan'])

## locate with index number

print(df_c.iloc[21])

#example .loc = for specific name 
print(df_c.loc['Japan',[1980,1981,1982,1983,1984]])
df_c.loc['Japan',1980:1984]
#example .iloc uses index number 
df_c.iloc[87,3:8]

# Filtering based on Conditions 

condition= df_c['Continent']== 'Asia'

print(df_c[condition])

# Visualization 

import matplotlib as mpl
import matplotlib.pyplot as plt

## Example: plot the line graph of Haiti from 1980:2013

import pandas as pd # primary data structure 
import numpy as np  # scinetific computing 

years= list(range(1980,2014))
haiti= df_c.loc["Haiti", years]
print(haiti)

haiti.plot()
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.text(2002,6500,'2010 Earthquake')
plt.show()














