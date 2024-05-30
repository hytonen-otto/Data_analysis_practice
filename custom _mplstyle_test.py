import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#print(mpl.matplotlib_fname())
plt.style.use("./styles/mystyle.mplstyle")
#plt.style.use("https://github.com/hytonen-otto/Data_analysis_practice/blob/4b05e91e2e210e63d9bf35e81ec51a297e59c66c/styles/mystyle.mplstyle") #Not working
#plt.style.use("seaborn-v0_8-whitegrid")

fig, ax = plt.subplots()
ax.set_title('Sine waves')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
for i in range(0,5):
    ax.plot(np.linspace(0,10,100),np.sin(i+np.linspace(0,10,100)),label=f'i value = {i}')
ax.legend()
plt.show()
