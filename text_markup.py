from types import LambdaType
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x_1 = np.linspace(0,5,10)
y_1 = x_1**2

ics_df = pd.read_csv('icecreamsales.csv')
ics_df = ics_df.sort_values(by='Temperature')

np_array = ics_df.values
x_2 = np_array[:,0]
y_2 = np_array[:,1]


fig_5 = plt.figure(figsize=(5,4), dpi=100)
axes_5 = fig_5.add_axes([0.1,0.1,0.9,0.9])

axes_5.text(0,23, r'$\alpha \beta \sigma \omega \epsilon \mu \pi \lambda$')
axes_5.text(0,18, r'$\delta_i \gamma^{ij} \sum_{i=0}^\infty x_i \frac{3}{4} $')
axes_5.text(0,13, r'$\frac{8 - \frac{x}{5}}{8} \sqrt{9} \sin(\pi) \sqrt[3]{8} \acute a \div  $')
axes_5.text(0,8, r'$ \bar a \hat a \tilde a \vec a \overline {a} \lim{x \to 2} f{x}  =5   $')
axes_5.text(0,3, r'$ \geq \leq \ne $')

axes_5.plot(x_1,y_1)

plt.show()