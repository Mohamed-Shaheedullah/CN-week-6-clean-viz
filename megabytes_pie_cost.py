import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

df_all = pd.read_excel("all.xlsx")

# df_all.drop(df_all.columns[0], axis=1)

df_all = df_all.drop(columns=["Unnamed: 0"])

print(df_all)

total_payments_df = df_all.groupby('Payment Method')['Cost'].sum().reset_index()
print(total_payments_df)

plt.pie(total_payments_df["Cost"],
        labels=total_payments_df["Payment Method"],
        autopct="%.1f%%", explode =[0,0,0,0,0.1],
        colors=["orange","green", "lightskyblue", "purple", "red"   ])
plt.title("Percent of Income from each Payment Method")

plt.show()
