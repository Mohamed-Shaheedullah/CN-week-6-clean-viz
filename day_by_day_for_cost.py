import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
debit = [142, 188.3, 153.9, 173.2, 189.1, 122.1, 149.2]
cash = [61.1, 102.9, 114.4, 87.7, 98.8, 131.3, 88]
credit = [20.9, 70.2, 48, 102.1, 76.8, 88.2, 23.3]
voucher = [13.7, 34.7, 44.9, 13.8, 30.5, 70.9, 20.1]
mobile_wallet = [39.6, 14.2, 49.3, 12.5, 15.7, 26.3, 15.8]

plt.plot(days, voucher,label="voucher")
plt.plot(days, mobile_wallet, label= "wobile wallet")
plt.legend()
plt.show()

