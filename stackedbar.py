import pandas as pd
import matplotlib.pyplot as plt


## make a dataframe from dictionary
df = pd.DataFrame({
    "Engineering":[56,13,1],
    "Computer Science":[77,23,4],
    "English Lit":[35,48,9],
    "Economics": [65,45,19]
}, index=["Male", "Female", "Non-Binary"])

## transpose frame 
df = df.T

my_plot = df.plot.barh(stacked=True)
plt.show()