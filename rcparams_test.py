import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#print(mpl.matplotlib_fname())
plt.style.use("./styles/mystyle.mplstyle")
#plt.style.use("seaborn-v0_8-whitegrid")

fig, ax = plt.subplots()
ax.set_title('Sine waves')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
for i in range(0,5):
    ax.plot(np.linspace(0,10,100),np.sin(i+np.linspace(0,10,100)))
plt.show()
