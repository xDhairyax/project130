import pandas as pd
import csv

df=pd.read_csv("merged_data.csv")

del df["Luminosity"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
del df["Star_name"]
print(df.shape)