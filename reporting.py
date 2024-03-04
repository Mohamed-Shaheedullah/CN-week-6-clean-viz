import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("f_h_sales_after.csv")
print(df)

profile = ProfileReport(df, title="Transaction Results After")

profile.to_file('results_report_after.html')