import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

df_all = pd.read_excel("all.xlsx")

# df_all.drop(df_all.columns[0], axis=1)

df_all = df_all.drop(columns=["Unnamed: 0"])

# print(df_all)

value_counts_df = df_all["Payment Method"].value_counts().reset_index()

plt.pie(value_counts_df["count"],
        labels=value_counts_df["Payment Method"],
        autopct="%.1f%%", explode =[0,0,0,0.1,0],
        colors=["lightskyblue", "orange", "green", "red", "purple"])
plt.title("Percent of Counts from each Payment Method")
plt.show()

# print(value_counts_df)
