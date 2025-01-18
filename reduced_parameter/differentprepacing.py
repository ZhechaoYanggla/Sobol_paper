#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 21:08:43 2023

@author: hgao
"""

import numpy as np
import matplotlib.pyplot as plt

# Error data
#error = np.array([1.983984467513955, 1.9115601792702572, 0.8927655264359381, 0.8562430263376127,
#                  0.7868138363516786, 0.4563855263525482, 0.31461143922299173, 0.19596459024565618,
#                  0.17802349605085177, 0.11314119008629923, 0.08266673770838164, 0])

lw=0.8

V15 = np.array([209.5, 214.7, 217.3, 219.40000000000003, 221.2, 222.90000000000003, 224.3, 225.60000000000002])





V14 = np.array([209.5, 214.7, 217.3, 219.40000000000003, 221.3, 222.90000000000003, 224.3, 225.60000000000002])





V13 = np.array([210.8, 216.2, 218.90000000000003, 220.90000000000003, 222.8, 224.40000000000003, 225.8, 227.0])






V12 = np.array([210.8, 216.2, 218.90000000000003, 220.90000000000003, 222.7, 224.3, 225.7, 227.0
])






V11 = np.array([209.40000000000003, 214.60000000000002, 217.2, 219.2, 221.10000000000002, 222.60000000000002, 224.0, 225.2
])




V10 = np.array([207.5, 212.40000000000003, 214.90000000000003, 216.8, 218.60000000000002, 220.2, 221.60000000000002, 222.8])




V9 = np.array([208.2, 213.10000000000002, 215.7, 217.8, 219.60000000000002, 221.2, 222.60000000000002, 223.8])

V8= np.array([204.90000000000003, 209.5, 212.10000000000002, 214.2, 216.10000000000002, 217.8, 219.3, 220.60000000000002])

V7 = np.array([198.8, 201.0, 201.7, 202.2, 202.7,203.10000000000002, 203.40000000000003,203.79999999999998])

V6 = np.array([186.40000000000003, 188.2, 189.3, 190.3, 191.2, 192.10000000000002,  193.0, 193.60000000000002])

V5 = np.array([184.7, 187.0, 188.2,  189.3, 190.3,191.2,192.0, 192.7])


t = np.array([300,400,500,600,700,800,900,1000])








plt.plot(t,V15,'k',alpha=0.7, marker = 'o', label = r'+$p_{\text{Kp}}$' ,linewidth=lw,linestyle='--')
plt.plot(t,V14,'b',alpha=0.7, marker = 'o', label=r'+$p_{\text{Na}}$',linewidth=lw)
#plt.plot(t,V13,'c',alpha=0.7, marker = 'o', label=r'+$p_{\text{Nab}}$',linewidth=lw)
#plt.plot(t,V12,'m',alpha=0.7, marker = 'o', label=r'+$p_{\text{Cap}}$', linewidth=lw)
plt.plot(t,V11, color='tab:brown',alpha=0.7, marker = 'o', label=r'+$p_{\text{tof}}$', linewidth=lw)
#plt.plot(t,V10, color='tab:gray',alpha=0.7, marker = 'o', label=r'+$p_{\text{Cab}}$', linewidth=lw)
plt.plot(t,V9,'g',alpha=0.7, marker = 'o', label= r'+$p_{\text{ClCa}}$', linewidth=lw)
plt.plot(t,V8,color='tab:orange',alpha=0.7, marker = 'o', label=r'+$p_{\text{tos}}$', linewidth=lw)
plt.plot(t,V7,'y',alpha=0.7, marker = 'o', label=r'+$p_{\text{NaK}}$', linewidth=lw)
plt.plot(t,V6,'r',alpha=0.7, marker = 'o', label=r'$p_{\text{Clb}} + p_{\text{Kr}} + p_{\text{K1}} + p_{\text{CaL}} + p_{\text{NaCa}} + p_{\text{Ks}}$', linewidth=lw)
plt.plot(t,V5,color='tab:gray',alpha=0.7, marker = 'o', label=r'$p_{\text{Clb}} + p_{\text{Kr}} + p_{\text{K1}} + p_{\text{CaL}} + p_{\text{NaCa}}$', linewidth=lw)
plt.xlabel('BCL [ms]', fontsize =12)
plt.ylabel('A$_{90}$ [ms]', fontsize =12)
plt.tick_params(axis='x', labelsize=12)
plt.tick_params(axis='y', labelsize=12)
plt.legend(loc='lower center',bbox_to_anchor=(0.5, -0.45),frameon=False, fontsize=12,ncol=3)
#plt.legend(loc='lower center',bbox_to_anchor=(0.5, -0.35),frameon=False, fontsize=12,ncol=3)
plt.savefig('Different_prepacing_reduced.pdf', bbox_inches='tight', pad_inches=0.1)
plt.show()
