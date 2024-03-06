import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

YT_time = [2,1,3,6,3]

Twitter_time = [1,1,0,0,2]

WhatsApp_time = [3,1,0,2,1]

RSL_time = [0,4,2,3,3]

TikTok_time = [3,0,1,0,2]

plt.plot(days, YT_time, label="YouTube", color='b', ls='dotted')
plt.plot(days, Twitter_time, label="Twitter", color='r', ls='--')
plt.plot(days, WhatsApp_time, label="WhatsApp", color ='c', ls='dashdot')
plt.plot(days, RSL_time, label="Raid Shadow Legends", color = 'y', linestyle='--', dashes=(5, 5))
plt.plot(days, TikTok_time, label="TikTok", color = 'k', linestyle='--', dashes=(5, 3))
plt.legend()
plt.show()

