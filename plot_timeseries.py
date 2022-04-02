from datetime import datetime
from types import LambdaType
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import datetime

goog_data = pd.read_csv('GOOG.csv')
goog_data_np = goog_data.to_numpy()
goog_cp = goog_data_np[:,4]

holidays = [datetime.datetime(2020,5,25), datetime.datetime(2020,8,19)]
date_arr = pd.bdate_range(start='5/20/2020', end='8/19/2020', freq='C', holidays=holidays)
date_arr_np = date_arr.to_numpy()
fig_7 = plt.figure(figsize=(8,5))
axes_7 = fig_7.add_axes([0.1,0.1,0.9,0.9])
plt.plot(date_arr_np, goog_cp)

plt.show()

