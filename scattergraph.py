import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

number_of_placements=np.array(list(range(1,11)))
responses_received = np.array([14, 21, 34, 36, 45, 51, 54, 63, 78, 92])


## plot exptl points 
plt.scatter(number_of_placements, responses_received)

m, c = np.polyfit(number_of_placements, responses_received, 1)
## plot x versus calculated y
plt.plot(number_of_placements, m * number_of_placements + c)


plt.title('Job Posting - Junior Dev Roles')
plt.xlabel("Number of places advertised")
plt.ylabel("Respnses received")
plt.show()
