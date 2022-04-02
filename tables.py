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


goog_data['Open'] = pd.Series([round(val, 2) for val in goog_data['Open']], index=goog_data.index)
goog_data['High'] = pd.Series([round(val, 2) for val in goog_data['High']], index=goog_data.index)
goog_data['Low'] = pd.Series([round(val, 2) for val in goog_data['Low']], index=goog_data.index)
goog_data['Close'] = pd.Series([round(val, 2) for val in goog_data['Close']], index=goog_data.index)
goog_data['Adj Close'] = pd.Series([round(val, 2) for val in goog_data['Adj Close']], index=goog_data.index)

print(goog_data)

stk_data = goog_data[-5:]
col_head = ('Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume')
stk_data_np = stk_data.to_numpy()
plt.figure(linewidth=2, tight_layout={'pad':.5})

axes_8 = plt.gca()
axes_8.get_xaxis().set_visible(False)
axes_8.get_yaxis().set_visible(False)

plt.box(on=None)

ccolors = plt.cm.Blues(np.full(len(col_head), 0.2))

the_table = plt.table(cellText=stk_data_np, loc='center', colLabels=col_head, colColours=ccolors)
the_table.set_fontsize(14)
the_table.scale(3, 2.5)

plt.show()





