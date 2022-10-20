import matplotlib as mpl
import matplotlib.pyplot as plt
print('Matplotlib version:', mpl.__version__)
import pandas as pd # primary data structure 
import numpy as np  # scinetific computing 

df_c = pd.read_excel("/Users/jonathancruz/Desktop/VS Code Workspace/Data Visualization /Canada.xlsx",
     sheet_name = 'Canada by Citizenship',
    skiprows= range(20),
    skipfooter= 2)

## cleaning dataset (### axis = 0 represents Rows, axis= 1 represents columns , default none = 0)
df_c.drop(['Type','Coverage', 'AREA','REG', 'DEV'], axis= 1 , inplace=True) 

# rename the columns 
df_c.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName' : 'Region'}, inplace=True)

# To rest , use df_c.reset_index()
df_c.set_index('Country', inplace=True )

years= list(range(1980,2014))

df_CI=df_c.loc[['India','China'],years]
df_CI


df_CI=df_CI.transpose()

df_CI.plot()
plt.title('Immigration from India and China')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()



