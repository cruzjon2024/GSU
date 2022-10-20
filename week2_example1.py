
#Example #1 - create a stacked area plot of the 5 countries that contributed to the least to immigrantion from 1980-2013, use alpha of 0.45
import pandas as pd 
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt

#Read file 
df_data= pd.read_excel("Data Visualization /Canada.xlsx",
                    sheet_name = 'Canada by Citizenship',
                    skiprows=range(20),
                    skipfooter= 2)

## Clean Dataset 

df_data.drop(["AREA", "REG","Type","DEV","Coverage"], axis=1 ,inplace=True)
df_data.rename(columns={'OdName':'Country',"AreaName":"Continent","RegName":"Region"}, inplace=True)

# sets index to countries 
df_data.set_index('Country', inplace = True)

years= list(range(1980,2014))

#ADD total column 
df_data["total"]= df_data.sum(axis=1)

df_data.sort_values(['total'], ascending = False , axis= 0 , inplace= True )

# #print(df_data.tail(5))

# df_bottom5=df_data.tail(5)
# df_bottom5= df_bottom5[years]
# df_bottom5=df_bottom5.transpose()


# df_bottom5.plot(kind='area',
#             stacked=False,
#             alpha= 0.45,
#             figsize=(15,8))

# plt.title('Immigration Trend of Bottom 5 Countries')
# plt.ylabel('Number of Immigrants')
# plt.xlabel('Years')
# plt.show()


## EXAMPLE : DISPLAY IMMIGRANT DIST FOR GREECE , ALBANIA, BULGARIA 
df_practice =df_data.loc[["Greece", "Albania", "Bulgaria"], years].transpose()
count, bin_edges= np.histogram(df_practice,15)
df_practice.plot(kind='hist',
                figsize=(10,5),
                bins =15,
                alpha=0.5,
                xticks=bin_edges,
                stacked=True,
                color=['coral','darkslateblue','mediumseagreen'])

plt.title('Histogram for Greece , Albania , and Bulgaria')
plt.ylabel("Number of years ")
plt.xlabel("Number of Immigrants ")
plt.show()


