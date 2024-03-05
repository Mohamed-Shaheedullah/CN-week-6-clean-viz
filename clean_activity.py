import pandas as pd
import openpyxl
df = pd.read_excel("cleaning_activity.xlsx")

df.info()


df = df.drop(columns=["Till ID", "Unnamed: 0"])

df = df.dropna(how="any")

df = df.set_index("Transaction ID")

# df["Transaction ID"]

# df = df.drop(df[df['Transaction ID'] = 56].index)

df = df.drop(56)


grp = df.groupby("Staff").sum("Cost")

# print(df)

print(grp)

# print(df)

mean_per_trans = (df["Cost"].mean())

print(f"Average price per transaction is {round(mean_per_trans, 2)} ")

def remove_punctuation(basket):
    basket = str(basket)
    basket=basket.replace("[", "")
    basket=basket.replace("]", "")
    basket=basket.replace("'", "")
    return basket

df["Basket"] = df["Basket"].apply(remove_punctuation)

def split_basket(basket_str):
    elements = basket_str.split(",")
    return [item.strip() for item in elements]

df["Basket"] = df["Basket"].apply(split_basket)

df = df.explode("Basket", ignore_index=False)


print(df["Basket"].value_counts())