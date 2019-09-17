import numpy as np
import matplotlib.pyplot as plt
f= np.loadtxt('shufflenet_acc_1_save.txt')
x=range(0,len(f))
plt.plot(x,f)
plt.show()

