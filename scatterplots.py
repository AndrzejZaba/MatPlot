from datetime import datetime
from types import LambdaType
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random


# Country array
cnt_arr = np.array(['Australia','Brazil','Canada','Chile','France','Germany','Greece',
                   'Iceland','India','Iran','Italy','Mexico','New Zealand','Nigeria',
                   'Norway','Pakistan','Peru','Russia','Saudi Arabia','Singapore',
                   'South Africa','Spain','Sweden','Turkey','UK','US'])
# Death rate per 100k Coronavirus
dr_arr = np.array([1.8,53,24.5,56.5,45.4,11.2,2.2,
                   2.8,4,24.6,58.6,46.3,.5,.5,
                   4.9,2.9,83.3,11,10.4,.5,
                   21.5,61.6,56.9,7.3,62.4,52.9])
# Daily confirmed cases (Tests)
test_arr = np.array([110,7197,600,1862,1636,1103,35,
                   10,295,1658,1226,2490,8,243,
                   48,1395,1101,4447,1443,280,
                   2830,1602,447,1205,1546,24988])
# Dot size Confirmed cases
cc_arr = np.array([24236,3456652,125408,390037,256534,229706,7684,
                   2035,2836925,350279,255278,537031,1654,50488,
                   10162,290445,549321,935066,302686,56031,
                   596060,370867,85411,253108,323008,5529824])


cc_arr_sm = cc_arr/1000
color_arr = np.random.rand(26)
plt.title('Death rate per 100k vs Confirmed Cases')
plt.xlabel('Death rate per 100k')
plt.ylabel('Confirmed Cases')
plt.scatter(dr_arr, test_arr, s=cc_arr_sm, c=color_arr, alpha=0.5)


plt.show()



