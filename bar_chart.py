from types import LambdaType
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x_1 = np.linspace(0,5,10)
y_1 = x_1**2

x = ['Nuclear', 'Hydro', 'Coal', 'Gas', 'Solar', 'Wind', 'Other']
per_1 = [71, 10, 3, 7, 2, 4, 3]
variance = [8, 3, 1, 3, 1, 2, 1]

#plt.bar(x, per_1, color = 'purple', yerr=variance )

m_eng = (76, 85, 86, 88, 93)
f_eng = (24, 15, 14, 12, 7)

spc = np.arange(5)
#plt.bar(spc, m_eng, width=0.45, label='Male', edgecolor='k')
#plt.bar(spc + 0.45, f_eng, width=0.45, label='Female', edgecolor='k')
#plt.xticks(spc + 0.45 /2, ('Areo', 'Chem', 'Civil', 'Elec', 'Mech'))


t_type = ['Kind', 'Elem', 'Sec', 'Spec']
m_teach = np.array([2, 20, 44, 14])
f_teach = np.array([98, 80, 56, 86])
ind = [x for x, _ in enumerate(t_type)]
plt.bar(ind, m_teach, width=0.45, label='Male', bottom=f_teach)
plt.bar(ind, f_teach, width=0.45, label='Female')
plt.legend(loc='lower right')


plt.show()

