import pandas as pd 
df=pd.read_csv("C:\\Users\\Arun kumar\\Desktop\\year.csv")
#print(df.head())


for i in range(9):
    df["prices"]=456
    df.to_csv("C:\\Users\\Arun kumar\\Desktop\\year.csv",index=False)




#df["prices"]=456
#df.to_csv("C:\\Users\\Arun kumar\\Desktop\\year.csv",index=False)
print(df.to_string())

#hi
