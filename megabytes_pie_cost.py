import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

df_all = pd.read_excel("all.xlsx")

total_payments_df = df_all.groupby('Payment Method')['Cost'].sum().reset_index()
print(total_payments_df)

plt.pie(total_payments_df["Cost"], labels=total_payments_df["Payment Method"], autopct="%.1f%%", explode =[0,0,0,0,0.1])
plt.show()