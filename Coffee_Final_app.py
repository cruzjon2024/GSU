import pandas as pd 
import numpy as np
import dateutil.parser as parser
import sys
import New_final as nf

coffee=pd.read_csv("/Users/jonathancruz/Desktop/VS Code Workspace/Data programming /Coffee Chain.csv",parse_dates=['Ddate'])

#print(coffee.dtypes)


#Data Cleaning 
coffee=coffee.drop("Number of Records", axis=1)
coffee["Ddate"].astype({'Ddate': 'datetime64[ns]'})
coffee["Budget Sales"].astype(int)
#coffee["Area Code"].astype(str)


c2 = coffee._get_numeric_data()
c2[c2 < 0] = 0

# u=coffee["Area Code"].unique()
# print(u)

if __name__ == "__main__":
    a=nf.Method1(coffee)
    print("Method 1.\n", a)

    
    b= nf.Method2(coffee)
    print("Method2.Area Code with Max profit:", b)


    d= nf.method4(coffee,5)
    print("Method4.(Q4):\n", d)

    e=nf.method5(coffee)
    print("Method5.\n", e)

