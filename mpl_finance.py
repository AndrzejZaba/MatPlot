from datetime import datetime
from types import LambdaType
from typing import ChainMap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

import mplfinance as mpf

goog_df = pd.read_csv('GOOG.csv', index_col = 0, parse_dates=True)
print(goog_df)
goog_df.index.name = 'Date'
mpf.plot(goog_df, type='ohlc', mav=(3,5,7), volume=True, show_nontrading=True)

plt.show()
