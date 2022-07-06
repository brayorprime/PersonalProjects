# solarpanelData.py
# Brayden Morse, 2022
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')

solarkW = np.array(data['Solar (kW)'])
homekW = np.array(data['Home (kW)'])
powerwallkW = np.array(data['Powerwall (kW)'])


time = np.linspace(0, 1440, 288)

plt.figure()
plt.plot(time, homekW, label = 'Home (kW)')
plt.plot(time, powerwallkW, label = 'Powerwall (kW)')
plt.plot(time, solarkW, label = 'Solar (kW)')
plt.ylabel('Power (kW)')
plt.xlim(0,max(time))
plt.grid()
plt.legend()




