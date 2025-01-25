import numpy as np
import math
import myokit
from scipy import integrate

from SALib.sample import saltelli
from SALib.analyze import sobol

import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, figsize=(12, 4))  

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




Cai15 = np.load('15_Cai.npy', mmap_mode='r+')

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







axs[0].plot(t,V6,'r',alpha=0.7, label=r"$\mathbf{y}^{\langle 6 \rangle}$", linewidth=lw)
axs[0].plot(t,V7,'y',alpha=0.7,label=r"$\mathbf{y}^{\langle 7 \rangle}$", linewidth=lw)
axs[0].plot(t,V8,color='tab:orange',alpha=0.7,  label=r"$\mathbf{y}^{\langle 8 \rangle}$", linewidth=lw)
axs[0].plot(t,V9,'g',alpha=0.7, label= r"$\mathbf{y}^{\langle 9 \rangle}$", linewidth=lw)
axs[0].plot(t,V10, color='tab:gray',alpha=0.7,  label=r"$\mathbf{y}^{\langle 10 \rangle}$", linewidth=lw)
axs[0].plot(t,V11, color='tab:brown',alpha=0.7,  label=r"$\mathbf{y}^{\langle 11 \rangle}$", linewidth=lw)
axs[0].plot(t,V12,'m',alpha=0.7,label=r"$\mathbf{y}^{\langle 12 \rangle}$", linewidth=lw)
axs[0].plot(t,V13,'c',alpha=0.7,  label=r"$\mathbf{y}^{\langle 13 \rangle}$",linewidth=lw)
axs[0].plot(t,V14,'b',alpha=0.7, label=r"$\mathbf{y}^{\langle 14 \rangle}$",linewidth=lw)
axs[0].plot(t,V15,'k',alpha=0.7, label = r"$\mathbf{y}$" ,linewidth=lw,linestyle='--')



axs[0].set_xlabel('t [ms]', fontsize =14)
axs[0].set_ylabel('V [mV]', fontsize =14)
axs[0].tick_params(axis='x', labelsize=14)
axs[0].tick_params(axis='y', labelsize=14)

axs[1].plot(t,Cai15,'k',alpha=0.7,linewidth=lw,linestyle='--')
axs[1].plot(t,Cai14,'b',alpha=0.7,linewidth=lw)
axs[1].plot(t,Cai13,'c',alpha=0.7,linewidth=lw)
axs[1].plot(t,Cai12,'m',alpha=0.7, linewidth=lw)
axs[1].plot(t,Cai11, color='tab:brown',alpha=0.7, linewidth=lw)
axs[1].plot(t,Cai10, color='tab:gray',alpha=0.7, linewidth=lw)
axs[1].plot(t,Cai9,'g',alpha=0.7, linewidth=lw)
axs[1].plot(t,Cai8,color='tab:orange',alpha=0.7, linewidth=lw)
axs[1].plot(t,Cai7,'y',alpha=0.7, linewidth=lw)
axs[1].plot(t,Cai6,'r',alpha=0.7, linewidth=lw)
axs[1].set_xlabel('t [ms]', fontsize =14)
axs[1].set_ylabel('[Ca$^{2+}]_{i}$ [mM]', fontsize =14)
axs[1].tick_params(axis='x', labelsize=14)
axs[1].tick_params(axis='y', labelsize=14)

APD9015 = np.array([209.5, 214.7, 217.3, 219.40000000000003, 221.2, 222.90000000000003, 224.3, 225.60000000000002])





APD9014 = np.array([209.5, 214.7, 217.3, 219.40000000000003, 221.3, 222.90000000000003, 224.3, 225.60000000000002])





APD9013 = np.array([210.8, 216.2, 218.90000000000003, 220.90000000000003, 222.8, 224.40000000000003, 225.8, 227.0])






APD9012 = np.array([210.8, 216.2, 218.90000000000003, 220.90000000000003, 222.7, 224.3, 225.7, 227.0
])






APD9011 = np.array([209.40000000000003, 214.60000000000002, 217.2, 219.2, 221.10000000000002, 222.60000000000002, 224.0, 225.2
])




APD9010 = np.array([207.5, 212.40000000000003, 214.90000000000003, 216.8, 218.60000000000002, 220.2, 221.60000000000002, 222.8])




APD909 = np.array([208.2, 213.10000000000002, 215.7, 217.8, 219.60000000000002, 221.2, 222.60000000000002, 223.8])

APD908= np.array([204.90000000000003, 209.5, 212.10000000000002, 214.2, 216.10000000000002, 217.8, 219.3, 220.60000000000002])

APD907 = np.array([198.8, 201.0, 201.7, 202.2, 202.7,203.10000000000002, 203.40000000000003,203.79999999999998])

APD906 = np.array([186.40000000000003, 188.2, 189.3, 190.3, 191.2, 192.10000000000002,  193.0, 193.60000000000002])

APD905 = np.array([184.7, 187.0, 188.2,  189.3, 190.3,191.2,192.0, 192.7])


tt = np.array([300,400,500,600,700,800,900,1000])








axs[2].plot(tt,APD9015,'k',alpha=0.7, marker = 'o' ,linewidth=lw,linestyle='--')
axs[2].plot(tt,APD9014,'b',alpha=0.7, marker = 'o',linewidth=lw)
axs[2].plot(tt,APD9013,'c',alpha=0.7, marker = 'o',linewidth=lw)
axs[2].plot(tt,APD9012,'m',alpha=0.7, marker = 'o', linewidth=lw)
axs[2].plot(tt,APD9011, color='tab:brown',alpha=0.7, marker = 'o', linewidth=lw)
axs[2].plot(tt,APD9010, color='tab:gray',alpha=0.7, marker = 'o', linewidth=lw)
axs[2].plot(tt,APD909,'g',alpha=0.7, marker = 'o', linewidth=lw)
axs[2].plot(tt,APD908,color='tab:orange',alpha=0.7, marker = 'o', linewidth=lw)
axs[2].plot(tt,APD907,'y',alpha=0.7, marker = 'o', linewidth=lw)
axs[2].plot(tt,APD906,'r',alpha=0.7, marker = 'o', linewidth=lw)
#axs[2].plot(t,APD905,color='tab:gray',alpha=0.7, marker = 'o', label=r'$p_{\text{Clb}} + p_{\text{Kr}} + p_{\text{K1}} + p_{\text{CaL}} + p_{\text{NaCa}}$', linewidth=lw)
axs[2].set_xlabel('BCL [ms]', fontsize =14)
axs[2].set_ylabel('A$_{90}$ [ms]', fontsize =14)
axs[2].tick_params(axis='x', labelsize=14)
axs[2].tick_params(axis='y', labelsize=14)

fig.legend(loc='outside lower center',bbox_to_anchor=(0.5, -0.25),frameon=False, fontsize=15,ncol=5)

plt.tight_layout()
plt.subplots_adjust(wspace=0.37,hspace=0.1)
# Save the combined figure as a PDF or display it
plt.savefig('fig070.pdf', bbox_inches='tight', pad_inches=0.1)
plt.show()
