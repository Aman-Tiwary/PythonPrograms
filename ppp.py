import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal
Time=1
fc=10
fs=44100
t=np.arange(0,Time,1/fs)
signal=np.sin(2*np.pi*(fc*t))
plt.plot(t,signal)
plt.xlabel('time')
plt.ylabel('fx')
plt.title('sine wave')
plt.show()
signal_f=np.fft.fft(signal)
plt.plot(t,signal_f)
plt.xlabel('time')
plt.ylabel('fx')
plt.title('fourier transform of sine wave')
plt.show()

#LTI SYSTEM
Time=0.5
fc=50
fs=44100
t=np.arange(0,Time,1/fs)
signal1=0.1*np.cos(2*np.pi*(fc*t))
plt.plot(t,signal1)
plt.xlabel('time')
plt.ylabel('fx')
plt.title('cosine wave')
plt.show()
signal_f1=np.fft.fft(signal1)
plt.plot(t,signal_f1)
plt.xlabel('time')
plt.ylabel('fx')
plt.title('fourier transform of cosine wave')
plt.show()

result=np.convolve(signal,signal1, mode='full')
plt.plot(result)
plt.xlabel('time')
plt.ylabel('fx')
plt.title('convolution of signals')
plt.show()
result_f=np.fft.fft(result)
plt.plot(result_f)
plt.xlim(0,2000)
plt.xlabel('time')
plt.ylabel('fx')
plt.title('frequency response of output')
plt.show()