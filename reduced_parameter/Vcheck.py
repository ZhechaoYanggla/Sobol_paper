import numpy as np
import math
import myokit
from scipy import integrate

from SALib.sample import saltelli
from SALib.analyze import sobol

import matplotlib.pyplot as plt

lw=0.8

V15 = np.load('15_V.npy', mmap_mode='r+')

V14 = np.load('14_V.npy', mmap_mode='r+')
V13 = np.load('13_V.npy', mmap_mode='r+')
V12 = np.load('12_V.npy', mmap_mode='r+')
V11 = np.load('11_V.npy', mmap_mode='r+')
V10 = np.load('10_V.npy', mmap_mode='r+')
V9 = np.load('9_V.npy', mmap_mode='r+')
V8= np.load('8_V.npy', mmap_mode='r+')
V7 = np.load('7_V.npy', mmap_mode='r+')
V6 = np.load('6_V.npy', mmap_mode='r+')

t = np.load('time.npy', mmap_mode='r+')

plt.plot(t,V15,'k',alpha=0.7, label = r'+$p_{\text{Kp}}$' ,linewidth=lw,linestyle='--')
plt.plot(t,V14,'b',alpha=0.7, label=r'+$p_{\text{Na}}$',linewidth=lw)
plt.plot(t,V13,'c',alpha=0.7,  label=r'+$p_{\text{Nab}}$',linewidth=lw)
plt.plot(t,V12,'m',alpha=0.7,label=r'+$p_{\text{Cap}}$', linewidth=lw)
plt.plot(t,V11, color='tab:brown',alpha=0.7,  label=r'+$p_{\text{tof}}$', linewidth=lw)
plt.plot(t,V10, color='tab:gray',alpha=0.7,  label=r'+$p_{\text{Cab}}$', linewidth=lw)
plt.plot(t,V9,'g',alpha=0.7, label= r'+$p_{\text{ClCa}}$', linewidth=lw)
plt.plot(t,V8,color='tab:orange',alpha=0.7,  label=r'+$p_{\text{tos}}$', linewidth=lw)
plt.plot(t,V7,'y',alpha=0.7,label=r'+$p_{\text{NaK}}$', linewidth=lw)
plt.plot(t,V6,'r',alpha=0.7, label=r'$p_{\text{Clb}} + p_{\text{Kr}} + p_{\text{K1}} + p_{\text{CaL}} + p_{\text{NaCa}} + p_{\text{Ks}}$', linewidth=lw)
plt.xlabel('t [ms]', fontsize =12)
plt.ylabel('V [mV]', fontsize =12)
plt.tick_params(axis='x', labelsize=12)
plt.tick_params(axis='y', labelsize=12)
plt.legend(loc='lower center',bbox_to_anchor=(0.5, -0.45),frameon=False, fontsize=12,ncol=3)
plt.savefig('Voltage.pdf', bbox_inches='tight', pad_inches=0.1)
plt.show()