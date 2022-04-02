from types import LambdaType
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x_1 = np.linspace(0,5,10)
y_1 = x_1**2

arr_1 = np.random.randint(1,7,7000)
arr_2 = np.random.randint(1,7,7000)
arr_3 = arr_1 + arr_2

plt.hist(arr_3, bins=11, density=True, stacked=True, color='black') #cumulative=True, orientation='horizontal', 

plt.show()
