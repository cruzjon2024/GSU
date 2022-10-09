# References :
#https://datatofish.com/multiple-linear-regression-python/ - Used to create regression analysis 

from ctypes.wintypes import INT
import pandas as pd
from sklearn import linear_model
from sqlalchemy import FLOAT
import re
import statsmodels.api as sm

## read CSV file
batting= pd.read_csv("batting_2.csv")

print(batting)
#Dropped name , team and player id - So i can change value from strings to floats
new_df2 = batting.drop(['Team','playerid','Name' ],1)
new_df2 = batting
print(new_df2)
print(new_df2.dtypes)

### may present float error 
#df =new_df2.astype(float)

# Regression analysis 
#Initial Regression model (26 variable model)
#x=new_df2[['MarApr_PA', 'MarApr_AB','MarApr_H','MarApr_HR','MarApr_R', 'MarApr_RBI', 'MarApr_SB','MarApr_BB%','MarApr_K%','MarApr_ISO','MarApr_BABIP','MarApr_AVG','MarApr_OBP','MarApr_SLG', 'MarApr_LD%','MarApr_GB%','MarApr_FB%','MarApr_IFFB%','MarApr_HR/FB','MarApr_O-Swing%','MarApr_Z-Swing%','MarApr_Swing%','MarApr_O-Contact%','MarApr_Z-Contact%','MarApr_Contact%']]

# 14 variable regression model 
x=new_df2[['MarApr_PA', 'MarApr_AB','MarApr_H','MarApr_K%','MarApr_ISO','MarApr_BABIP','MarApr_AVG','MarApr_SLG', 'MarApr_HR/FB','MarApr_O-Swing%','MarApr_Z-Swing%','MarApr_Swing%','MarApr_O-Contact%','MarApr_Z-Contact%','MarApr_Contact%']]
y=new_df2[['FullSeason_OBP']]

regr= linear_model.LinearRegression()
regr.fit(x, y)

print('Intercept: \n ',regr.intercept_)
print('Coefficients: \n', regr.coef_)

x = sm.add_constant(x)

## prints Regression analysis 
model= sm.OLS(y,x).fit()
predictions = model.predict(x)

print_model = model.summary()

print(print_model)

### dropped columns with high p-values and little signfigance to OBP(y variable)
new_df3 = new_df2.drop(['Team','MarApr_HR','MarApr_R','MarApr_RBI','MarApr_SB','MarApr_BB%','MarApr_LD%','MarApr_GB%','MarApr_FB%','MarApr_IFFB%',],1)

print(new_df3)

### create a CSV file for Tableau 
new_df3.to_csv("new_batting1.csv", index=False)


