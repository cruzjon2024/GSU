#Area Plot , Bar plot 
#%%
from matplotlib.patches import ArrowStyle, ConnectionStyle
import pandas as pd 
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt

df_data= pd.read_excel("Data Visualization /Canada.xlsx",
                    sheet_name = 'Canada by Citizenship',
                    skiprows=range(20),
                    skipfooter= 2)

## Clean Dataset 

df_data.drop(["AREA", "REG","Type","DEV","Coverage"], axis=1 ,inplace=True)
df_data.rename(columns={'OdName':'Country',"AreaName":"Continent","RegName":"Region"}, inplace=True)


df_data.set_index('Country', inplace = True)

print(df_data.head(5))

years= list(range(1980,2014))


#Visualizing Data using Matplotlib 
# option to look like R, matplotlib.pyplot as plt 
#mpl.style.use('ggplot')

#Area plot 
# create a stacked area plot of the top 5 countries that contributed the most to immigration in Canada 1980-2013

#ADD total column 

df_data["total"]= df_data.sum(axis=1)


df_data.sort_values(['total'], ascending = False , axis= 0 , inplace= True )
print(df_data.head(5))

#To get top 5 entries 
df_top5= df_data.head(5)
print(df_top5)
# Top 5 years ONLY
df_top5= df_top5[years]


# transpose - create a column for each country 

df_top5= df_top5.transpose()

print(df_top5.head())

# plot each country 

# df_top5.plot(kind='area',
#             stacked=False,
#             figsize=(15,8))

# plt.title('Immigration Trend of Top 5 Countries')
# plt.ylabel('Number of Immigrants')
# plt.xlabel('Years')
# plt.show()

# pplot by ocuntry stacked
# df_top5.plot(kind='area',
#             stacked=True,
#             figsize=(15,8))

# plt.title('Immigration Trend of Top 5 Countries')
# plt.ylabel('Number of Immigrants')
# plt.xlabel('Years')
# plt.show()

# pplot with diffrent transparancy 
# df_top5.plot(kind='area',
#             stacked=True,
#             alpha =0.25, #0-1 , defualt alpah 0.5
#             figsize=(15,8))

# plt.title('Immigration Trend of Top 5 Countries')
# plt.ylabel('Number of Immigrants')
# plt.xlabel('Years')
# plt.show()


##HISTOGRAM DIST FREQUENCY OF NUMERICAL DATASET
# Find and plot the frequency distribution of the population (numbers) o fthe new immigrants from varoius countries from canada from 2013 

# print(df_data[2013].head())

# #np.histogram returns to values 
# count, bin_edges = np.histogram(df_data[2013])

# print(count) #Frequency Count 
# print(bin_edges) # bin ranges, default = 10 bins 

# #Plot histogram 

# df_data[2013].plot( kind='hist', figsize=(8,5))
# plt.title('Histogram of immigrant in 2013')
# plt.ylabel("Number of Countries")
# plt.xlabel("Number of Immigrants ")
# plt.show()


## FIXED HISTOGRAM with bin edges 
# count, bin_edges = np.histogram(df_data[2013])
# df_data[2013].plot( kind='hist', figsize=(8,5) , xticks=bin_edges)


# df_data[2013].plot( kind='hist', figsize=(8,5))
# plt.title('Histogram of immigrant in 2013')
# plt.ylabel("Number of Countries")
# plt.xlabel("Number of Immigrants ")
# plt.show()


## EXAMPLE : WHAT IS THE IMMIGRATION DIST FOR DENMARK, NORWAY, SWEDEN FOR 1980-2013 - will show all years 
# df_new=df_data.loc(['Denmark','Sweden','Norway'],years)

# df_data.plot.hist()

# Need to transpose - need just total 
#df_new=df_data.loc[['Denmark','Sweden','Norway'],years].transpose()
# df_new.plot.hist()
# plt.title('Histogram for Sweden , Norway , and Denmark')
# plt.ylabel("Number of years ")
# plt.xlabel("Number of Immigrants ")
# plt.show()

# CHNAGE BIN SIZE AND ADD COLOR 
# df_new=df_data.loc[['Denmark','Sweden','Norway'],years].transpose()
# count, bin_edges= np.histogram(df_new,15)
# df_new.plot(kind='hist',
#             figsize=(10,6),
#             bins =15,
#             alpha=0.5,
#             xticks=bin_edges,
#             color=['coral','darkslateblue','mediumseagreen'])

# plt.title('Histogram for Sweden , Norway , and Denmark')
# plt.ylabel("Number of years ")
# plt.xlabel("Number of Immigrants ")
# plt.show()

#MODIFICATIONS 
# df_new=df_data.loc[['Denmark','Sweden','Norway'],years].transpose()
# count, bin_edges= np.histogram(df_new,15)
# df_new.plot(kind='hist',
#             figsize=(10,5),
#             bins =15,
#             alpha=0.5,
#             xticks=bin_edges,
#             stacked=True,
#             color=['coral','darkslateblue','mediumseagreen'])

# plt.title('Histogram for Sweden , Norway , and Denmark')
# plt.ylabel("Number of years ")
# plt.xlabel("Number of Immigrants ")
# plt.show()


#BAR PLOT 
#Filter data 

# df_iceland= df_data.loc["Iceland", years ]

# df_iceland.plot(kind='bar', figsize=(10,5))
# plt.title('ICELAND')
# plt.ylabel("Number of immigrants")
# plt.xlabel("Years")
# plt.show()

#horizontal Bar graph 
# df_iceland= df_data.loc["Iceland", years ]

# df_iceland.plot(kind='barh', figsize=(10,5))
# plt.title('ICELAND')
# plt.ylabel("Number of immigrants")
# plt.xlabel("Years")
# plt.show()

#ADD ANNOTATION FOR FIANCIAL CRISIS

df_iceland= df_data.loc["Iceland", years ]

df_iceland.plot(kind='bar', figsize=(10,5))
plt.title('ICELAND')
plt.ylabel("Number of immigrants")
plt.xlabel("Years")
plt.annotate('', #string(text)
            xy= (32,70), # place arrow at this point 32= 2012 and top is 70 
            xytext=(28,20), # place base of the arrow at point years 28 = 2008 , top 20 
            xycoords='data', #use coordinate system of teh object being annotated 
            arrowprops=dict(arrowstyle = '->', connectionstyle='arc3', color='blue',lw=2)
            )
plt.annotate('2008 - 2011 Financial Crisis',
            xy=(28,30),
            rotation=72.5,
            va= 'bottom',
            ha= 'left')          
plt.show()



# %%
