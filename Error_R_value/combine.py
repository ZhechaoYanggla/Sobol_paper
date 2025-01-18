#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 21:08:43 2023

@author: hgao
"""

import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 1, figsize=(6, 4))  

# Error data
#error = np.array([1.983984467513955, 1.9115601792702572, 0.8927655264359381, 0.8562430263376127,
#                  0.7868138363516786, 0.4563855263525482, 0.31461143922299173, 0.19596459024565618,
#                  0.17802349605085177, 0.11314119008629923, 0.08266673770838164, 0])



Rvalue = np.array([0.4369555836279964, 0.5099571716456495, 0.5132538668002712, 0.6889962316837188, 0.7447946149813967, 0.7482705366794922, 0.7638309212533065, 0.8348135066537555, 0.8521743543736888,1])

error = np.array([0.8927655264359381, 0.8562430263376127,
                  0.7868138363516786, 0.4563855263525482, 0.31461143922299173, 0.19596459024565618,
                  0.17802349605085177, 0.11314119008629923, 0.08266673770838164, 0])




# Corresponding labels
labels = [r'$p_{\text{Clb}} + p_{\text{Kr}} + p_{\text{K1}} + p_{\text{CaL}} + p_{\text{NaCa}} + p_{\text{Ks}}$', r'+$p_{\text{NaK}}$', r'+$p_{\text{tos}}$',
          r'+$p_{\text{ClCa}}$', r'+$p_{\text{Cab}}$', r'+$p_{\text{tof}}$', r'+$p_{\text{Cap}}$', r'+$p_{\text{Nab}}$', r'+$p_{\text{Na}}$', r'+$p_{\text{Kp}}$']

# Create the plot
axs[0].plot(error, marker='o')  # Adding marker for better visualization
axs[0].set_xticks(np.arange(len(error)))
#axs[0].set_xticklabels(labels, fontsize=12, rotation=45, ha='right')


axs[0].tick_params(axis='x', labelsize=12, pad=2)
axs[0].tick_params(axis='y', labelsize=12, pad=2)
axs[0].set_ylabel('Error', fontsize=12)


axs[1].plot(Rvalue, marker='o')  # Adding marker for better visualization
axs[1].set_xticks(np.arange(len(error)))
axs[1].set_xticklabels(labels, fontsize=12, rotation=45, ha='right')


axs[1].tick_params(axis='x', labelsize=12, pad=2)
axs[1].tick_params(axis='y', labelsize=12, pad=2)
axs[1].set_ylabel('R value', fontsize=12)


plt.tight_layout()
plt.subplots_adjust(wspace=0.37,hspace=0.1)
# Save the combined figure as a PDF or display it
plt.savefig('combined_figure.pdf', bbox_inches='tight', pad_inches=0.1)
plt.show()