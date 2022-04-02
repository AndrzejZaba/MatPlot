from types import LambdaType
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x_1 = np.linspace(0,5,10)
y_1 = x_1**2
plt.plot(x_1,y_1)
plt.title('Days Squared Chart')
plt.xlabel('Days')
plt.ylabel('Days squared')
plt.subplot(1,2,1)
plt.plot(x_1,y_1,'r')
plt.subplot(1,2,2)
plt.plot(x_1,y_1,'b')

fig_1 = plt.figure(figsize=(5,4), dpi=100)
axes_1 = fig_1.add_axes([0.1, 0.1, 0.9, 0.9])
axes_1.set_xlabel('Days')
axes_1.set_ylabel('Days Squared')
axes_1.set_title('Days Squared Chart')
axes_1.plot(x_1, y_1, label='x/x^2')
axes_1.plot(y_1, x_1, label='x^2/x')
axes_1.legend(loc=0)    # programme will automatically choose the best location for legend
# upper right: 1, upper left: 2, lower left: 3, lower right: 4 
# or supply a tuple of x & y from lower screen (sth like coords)

axes_2 = fig_1.add_axes([0.45, 0.45, 0.4, 0.3])
axes_2.set_xlabel('Days')
axes_2.set_ylabel('Days Squared')
axes_2.set_title('Days Squared Chart')
axes_2.plot(x_1, y_1, 'r')

axes_2.text(0,40,'Message')


plt.show()








