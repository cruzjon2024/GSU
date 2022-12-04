from matplotlib.patches import ArrowStyle, ConnectionStyle
import pandas as pd 
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Atleast 5 diffrent visuals 


# #Original CSV
# df_sneakers = pd.read_excel(
#     'Data Visualization /StockX-Data.xlsx',
#     sheet_name='Raw Data')


# #change time to datetime 
# df_sneakers['Release Date'] = pd.to_datetime(df_sneakers['Release Date'])
# df_sneakers['Order Date'] = pd.to_datetime(df_sneakers['Order Date'])

# # Create 3 columsn to track total revenue and time to sale item(months and days )
# df_sneakers["Profit"]= (df_sneakers['Sale Price']- df_sneakers["Retail Price"])
# df_sneakers['Time to sale ']= (df_sneakers["Order Date"] - df_sneakers["Release Date"]) # in days 
# df_sneakers['Months to sale ']= ((df_sneakers["Order Date"] - df_sneakers["Release Date"])/ np.timedelta64(1, 'M')).astype(int) # in months 

# # DROP ORDER DATE
# df_s=df_sneakers.drop(columns=['Order Date'])


# df_ow=df_sneakers[df_sneakers["Brand"]== "Off-White"] #ONLY Nike or OFFwhite
# df_y=df_sneakers[df_sneakers["Brand"] != "Off-White"] #ONLY yeezy

# #Created a CSV grouped by brand and after cleaning with new columns 

# df_ow.to_csv('off_white.csv')
# df_y.to_csv('yeezy.csv')
# df_s.to_csv('Sneakers.csv')


#New cleaned CSV with both brands 
df_s = pd.read_csv(
    'Sneakers.csv')

df_s=df_s.drop(columns=['Unnamed: 0'])
print(df_s.head())

#Clean Data Again 
df_s['Sneaker Name'] = df_s['Sneaker Name'].apply(lambda x: x.replace('-', ' '))
#print(df_s.dtypes)

df_s["Brought for below Retail"]= df_s['Sale Price']<df_s['Retail Price']
df_s["Brought for Retail"]= df_s['Sale Price']== df_s['Retail Price']
df_s["Brought for above Retail"]= df_s['Sale Price']>df_s['Retail Price']

print(df_s)

#Correlation Map 
fig, ax = plt.subplots(figsize=(10, 8))

correlations = df_s.corr()
sns.heatmap(correlations,annot=True)
#plt.show()

##Group by of Total Profit and brand 

#print(df_s.groupby(['Brand']).sum())
#df_s.groupby('Brand')['Profit'].sum()

##Groupby brand and average the shoe size
#print(df_s.groupby('Brand')['Shoe Size'].mean())

##group by for specific models 
#print(df_s.groupby(['Sneaker Name']).sum())

## Groupby sneaker model and average shoe size 
#print(df_s.groupby('Sneaker Name')['Shoe Size'].mean())
#print(df_s.describe())


#df_need = ['Release Date', 'Buyer Region', 'Sneaker Name', 'Retail Price', 'Shoe Size', 'Brand', 'Brought for Retail', 'Brought for below Retail', 'Brought for above Retail' ]

df_need = [   'Shoe Size']
for s in df_need:
    snk_num= df_s[str(s)].value_counts() 
    plt.figure(figsize=(10,8))
    s_chart= sns.barplot(x=snk_num.index,y=snk_num)
    s_chart.set_title("Sneakers Sales by %s" % (s))
    plt.ylabel("Sneaker Sales")
    s_chart.set_xticklabels(s_chart.get_xticklabels(), rotation = 90)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
    plt.show()


#print(snk_num)

