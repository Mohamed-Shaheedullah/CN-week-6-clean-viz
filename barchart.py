import pandas as pd
import matplotlib.pyplot as plt

## make a dataframe from dictionary
df = pd.DataFrame({
    "Locations" : [
    "Twitter",
    "Facebook",
    "LinkedIn",
    "Indeed",
    "Instagram"
],
    "Responses" : [3,11,16,13,2],
})

df = df.sort_values("Responses")
bar_colors = ['red' if x == df['Responses'].max() else 'blue' for x in df['Responses']] ## creates a list by l comp
plt.bar("Locations", "Responses", data=df, color=bar_colors)
##barh for horizontal and swap labels
plt.title("Return from job psoting by location")
plt.xlabel("Advert Location")
plt.ylabel("Applications Received")

# print(bar_colors)
plt.show()