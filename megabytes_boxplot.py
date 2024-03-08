import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

df_all = pd.read_excel("all.xlsx")

# df_all.drop(df_all.columns[0], axis=1)
b_plot = df_all.boxplot(column = 'Cost') 
plt.title("Boxplot for Cost")
plt.show()
