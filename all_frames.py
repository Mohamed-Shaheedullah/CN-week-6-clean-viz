import pandas as pd
from ydata_profiling import ProfileReport
import matplotlib.pyplot as plt
import openpyxl
import numpy as np

df1 = pd.read_excel(r"./megabytes_data/monday_graph.xlsx")
df2 = pd.read_excel(r"./megabytes_data/tuesday_graph.xlsx")
df3 = pd.read_excel(r"./megabytes_data/wednesday_graph.xlsx")
df4 = pd.read_excel(r"./megabytes_data/thursday_graph.xlsx")
df5 = pd.read_excel(r"./megabytes_data/friday_graph.xlsx")
df6 = pd.read_excel(r"./megabytes_data/saturday_graph.xlsx")
df7 = pd.read_excel(r"./megabytes_data/sunday_graph.xlsx")

df1['Day'] = 'Monday'
df2['Day'] = 'Tuesday'
df3['Day'] = 'Wednesday'
df4['Day'] = 'Thursday'
df5['Day'] = 'Friday'
df6['Day'] = 'Saturday'
df7['Day'] = 'Sunday'

df_all = pd.concat([df1,df2,df3,df4,df5, df6,df7], ignore_index=True)

# profile = ProfileReport(df_all, title="Megabytes Profile")

# profile.to_file('megabytes_report_before.html')

df_all = df_all.dropna(how="any")
df_all = df_all.drop(columns=["Unnamed: 0"])

# profile = ProfileReport(df_all, title="Megabytes Profile")

# profile.to_file('megabytes_report_after.html')

# print(df_all)

# df_all.to_excel("all.xlsx")

# print(df_all.info())

# print(df_all.describe())

# print(df_all["Payment Method"].value_counts())

# print(df_all.groupby("Payment Method").sum("Cost"))


