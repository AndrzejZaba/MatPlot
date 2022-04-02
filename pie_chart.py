from types import LambdaType
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

fig_6 = plt.figure(figsize=(8,5), dpi=100)
axes_6 = fig_6.add_axes([0.1, 0.1, 0.9, 0.9])

# Create a pie chart of the number of pokemon by type
types = ['Water', 'Normal', 'Flying', 'Grass', 'Phisic', 'Bug', 'Fire', 'Poison', 'Ground', 'Rock', 'Fighting', 'Dark', 'Steel', 'Electric', 'Dragon', 'Fairy', 'Ghost', 'Ice']
poke_num = [133, 109, 101, 98, 85, 77, 68, 66, 65, 60, 57, 54, 53, 51, 50, 50, 46, 40]

colors = []
for i in range(18):
    rgb = (random.uniform(0,.5),random.uniform(0,.5),random.uniform(0,.5))
    colors.append(rgb)

explode = [0] * 18
explode[0] = 0.2
wedges, texts, autotexts = plt.pie(poke_num, explode=explode, labels=types, colors=colors, autopct='%1.0f%%', shadow=True, startangle=140, textprops=dict(color='w'))
plt.legend(wedges, types, loc='right', bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()