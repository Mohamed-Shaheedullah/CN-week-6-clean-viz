import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

df_all = pd.read_excel("all.xlsx")

# df_all.drop(df_all.columns[0], axis=1)

df_all = df_all.drop(columns=["Unnamed: 0"])

total_payments_df = df_all.groupby(['Day', 'Payment Method'])['Cost'].sum().reset_index()

print(total_payments_df)

#  my_plot = df_all.plot.barh(stacked=True)

#  plt.show()


