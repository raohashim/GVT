import matplotlib, scipy
import numpy as np
from numpy import sin, pi
from matplotlib import pyplot as plt
from scipy import signal
#for sawtooth plot
tooth=np.linspace(-np.pi,np.pi,500)
plt.plot(tooth, signal.sawtooth(2 * np.pi * 2 * tooth))
#for sine waves plot
x=np.linspace(-np.pi,np.pi,180)
plt.plot(x,np.sin(2*x))
#for ploting of the graph and labeling  
plt.xlabel('Period')
plt.ylabel('Amplitude')
plt.legend(('tooth','sine'))
plt.grid(True)
plt.title(('Sine and Sawtooth'))
#for form black horizontal 
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.ylim(-2, 2)
plt.show()

