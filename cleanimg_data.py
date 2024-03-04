import pandas as pd
import openpyxl
df = pd.read_excel("first_hour_sales.xlsx")

# df.to_csv("f_h_sales_before.csv", index=False)

# print(df)
# print(df.describe())

df = df.set_index("Transaction ID")

df = df.drop(columns=["Till ID"])



df = df.drop([16,17,18])


df = df.drop_duplicates()


# print(df.describe())

df.at[12,"Amount"] = 3.10

print(df)

def float_to_time(stamp):
    stamp = str(stamp)
    stamp = stamp.replace(".", ":")
    stamp = "0" + stamp
    if len(stamp) != 5:
        stamp=stamp + "0"
    return stamp
    # print(stamp)


df["Time"] = df["Time"].apply(float_to_time)

# print(df)


df["Time"] = pd.to_datetime(df["Time"])

# print(df)
# df.to_csv("f_h_sales_after.csv")




# ## average price of an item
# mean_price = df["Amount"].mean()
# print(f"The mean item price is {round(mean_price, 2)}")

# ## average basket price 
# my_ave_bkt = (sum(df["Amount"] * df["Items"])) / df.shape[0]

# print(f"The average basket price is {round(my_ave_bkt, 2)}")

# ## max and min spend in one transaction

# df = df.assign(Total = df["Amount"] * df["Items"])

# # print(df2)

# my_max = df["Total"].max()
# my_min = df["Total"].min()

# print(f"The max spend in one transaction is {my_max}")

# print(f"The min spend in one transaction is {my_min}")

# ## the most common spend amount

# common_spend = df["Total"].mode()

# print(f"The most common spend amount is {common_spend} ")

# ## the most common payment type

# common_payment = df["Currency"].mode()
# print(f"The most common payment type is {common_payment} ")

#John's answers

print("Johns answers")

sum_amount = df["Amount"].sum()
sum_items = df["Items"].sum()

average_item_price = sum_amount / sum_items

print(f"average is {average_item_price}")

mean_basket = df["Amount"].mean()

print(f"mean basket is {mean_basket}")


print("Max spend")
print(df["Amount"].max())

print("Min spend")
print(df["Amount"].min())

print("Most common spend")
print(df["Amount"].mode())

print("most common payment type")
print(df["Currency"].mode()[0])
