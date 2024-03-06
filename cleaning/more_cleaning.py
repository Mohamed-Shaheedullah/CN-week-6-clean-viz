import pandas as pd
df = pd.read_excel("cleaning_data.xlsx")

df = df.drop(columns=["Unnamed: 0", "Till ID"])

df=df.drop([0])

print(df["Transaction Type"].value_counts())

df = df.dropna(how="any")


# def replace_items(row):
#     if row.isna().any():
#         return 0
#     else:
#         return row["Total Items"]

# df["Total Items"] = df.apply(replace_items, axis=1)

print(df)

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





