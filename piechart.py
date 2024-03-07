import pandas as pd
import matplotlib.pyplot as plt

roles = [    
    "Front-end", 
    "Back-end",
    "Full-stack",
    "DevOps"
    ]

employees = [52,36,28,11]

plt.pie(employees, labels=roles, autopct="%.1f%%", explode=[0,.1,0,0])
plt.show()