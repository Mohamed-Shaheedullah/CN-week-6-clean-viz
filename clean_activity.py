import pandas as pd
import openpyxl
df = pd.read_excel("cleaning_activity.xlsx")

# df.info()


df = df.drop(columns=["Till ID", "Unnamed: 0"])

df = df.dropna(how="any")
df = df.drop_duplicates()


## question 1 
def staff_to_lowercase(employee):
    employee = str(employee)
    return employee.lower()

df["Staff"] = df["Staff"].apply(staff_to_lowercase)

df = df.set_index("Transaction ID")


## delete outlier
df = df.drop(56)

## find staff MVP (by cost)
grp = df.groupby("Staff").sum("Cost")

new_df = grp.sort_values(by = ['Cost'], ascending=[False])


print(f" Staff MVP by cost {new_df.iloc[0]}")


## find average cost per transaction

mean_per_trans = (df["Cost"].mean())

print(f"Average price per transaction is {round(mean_per_trans, 2)} ")

## explode basket

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

# print(df["Basket"].value_counts(ascending=True) prints whole lists

print("Least popular item")
print(df["Basket"].value_counts(ascending=True).index[0])
