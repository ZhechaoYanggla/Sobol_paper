import numpy as np
import math
import myokit
from scipy import integrate

from SALib.sample import saltelli
from SALib.analyze import sobol

import matplotlib.pyplot as plt

lw=0.8

V15 = np.load('15_Cai.npy', mmap_mode='r+')

Cai14 = np.load('14_Cai.npy', mmap_mode='r+')
Cai13 = np.load('13_Cai.npy', mmap_mode='r+')
Cai12 = np.load('12_Cai.npy', mmap_mode='r+')
Cai11 = np.load('11_Cai.npy', mmap_mode='r+')
Cai10 = np.load('10_Cai.npy', mmap_mode='r+')
Cai9 = np.load('9_Cai.npy', mmap_mode='r+')
Cai8= np.load('8_Cai.npy', mmap_mode='r+')
Cai7 = np.load('7_Cai.npy', mmap_mode='r+')
Cai6 = np.load('6_Cai.npy', mmap_mode='r+')

t = np.load('time.npy', mmap_mode='r+')

plt.plot(t,Cai15,'k',alpha=0.7, label = r'+$p_{\text{Kp}}$' ,linewidth=lw,linestyle='--')
plt.plot(t,Cai14,'b',alpha=0.7, label=r'+$p_{\text{Na}}$',linewidth=lw)
plt.plot(t,Cai13,'c',alpha=0.7,  label=r'+$p_{\text{Nab}}$',linewidth=lw)
plt.plot(t,Cai12,'m',alpha=0.7,label=r'+$p_{\text{Cap}}$', linewidth=lw)
plt.plot(t,Cai11, color='tab:brown',alpha=0.7,  label=r'+$p_{\text{tof}}$', linewidth=lw)
plt.plot(t,Cai10, color='tab:gray',alpha=0.7,  label=r'+$p_{\text{Cab}}$', linewidth=lw)
plt.plot(t,Cai9,'g',alpha=0.7, label= r'+$p_{\text{ClCa}}$', linewidth=lw)
plt.plot(t,Cai8,color='tab:orange',alpha=0.7,  label=r'+$p_{\text{tos}}$', linewidth=lw)
plt.plot(t,Cai7,'y',alpha=0.7,label=r'+$p_{\text{NaK}}$', linewidth=lw)
plt.plot(t,Cai6,'r',alpha=0.7, label=r'$p_{\text{Clb}} + p_{\text{Kr}} + p_{\text{K1}} + p_{\text{CaL}} + p_{\text{NaCa}} + p_{\text{Ks}}$', linewidth=lw)
plt.xlabel('t [ms]', fontsize =12)
plt.ylabel('[Ca$^{2+}]_{i}$ [mM]', fontsize =12)
plt.tick_params(axis='x', labelsize=12)
plt.tick_params(axis='y', labelsize=12)
#plt.legend(loc='lower center',bbox_to_anchor=(0.5, -0.35),frameon=False, fontsize=12,ncol=3)
plt.savefig('Cai.pdf', bbox_inches='tight', pad_inches=0.1)
plt.show()