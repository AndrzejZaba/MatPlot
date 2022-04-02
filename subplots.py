from types import LambdaType
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x_1 = np.linspace(0,5,10)
y_1 = x_1**2

figure_2, axes_2 = plt.subplots(figsize = (8,4), nrows=1, ncols=3)
plt.tight_layout()
axes_2[1].set_title('Plot 2')
axes_2[1].set_xlabel('X')
axes_2[1].set_ylabel('X squared')
axes_2[1].plot(x_1,y_1)
axes_2[0].plot(x_1*4,y_1,'r')
axes_2[2].plot(x_1,y_1,'k')

# Default colors (b: blue, g: green, r: red, c: cyan, m: magenta, y: yellow, k: black, w: white)
# color="0.75" creates a 75% gray
# You can use hexcodes color="#eeefff"
# You can color names found next ike this color = "blurywood"

fig_3 = plt.figure(figsize=(6,4))
axes_3 = fig_3.add_axes([0.1,0.1,0.9,0.9])
axes_3.plot(x_1,y_1, color="navy", alpha=.75, lw=2, ls='-.', marker='o', markersize=7, markerfacecolor='y', markeredgecolor='r', markeredgewidth='1')        # ls - line style

axes_3.set_xlim([0,3])
axes_3.set_ylim([0,8])

axes_3.grid(True, color='0.6', dashes=(5,2,1,2))
axes_3.set_facecolor('#FAEBD7')

fig_3.savefig('3rd_plot.png')


ics_df = pd.read_csv('icecreamsales.csv')
ics_df = ics_df.sort_values(by='Temperature')
print(ics_df)

np_array = ics_df.values
x_2 = np_array[:,0]
y_2 = np_array[:,1]
fig_4 = plt.figure(figsize=(6,5))
axes_4 = fig_4.add_axes([0.05,0.05,0.95,0.95])
axes_4.set_xlabel('Temperature')
axes_4.set_ylabel('Sales')
axes_4.set_title('Icecream sales vs Temperature')
axes_4.plot(x_2,y_2)

axes_4.annotate('Good Month', xy=(83,536), xytext=(60,520), arrowprops=dict(facecolor='black', shrink=0.05))

plt.bar(x_2,y_2)
plt.show()

