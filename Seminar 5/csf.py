import numpy as np
import matplotlib.pyplot as plt

def csf(f):
	return 2.6*(0.114*f)*np.exp(-0.114*f)


f= np.arange(0,40,0.1)
plt.plot(f,csf(f))
plt.ylabel('CSF')
plt.xlabel('Frequncy')
plt.show()
