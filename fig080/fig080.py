import numpy as np
import math
import myokit
from scipy import integrate

from SALib.sample import saltelli
from SALib.analyze import sobol

import matplotlib.pyplot as plt
from SALib.plotting.bar import plot as barplot

x=np.arange(0,500,1)
y=x
YNS = np.load('apd90_NS.npy', mmap_mode='r+')
YR = np.load('apd90_R.npy', mmap_mode='r+')

YS = np.load('apd90_S.npy', mmap_mode='r+')


target = np.where(YR<499)
YR = YR[target]
YNS = YNS[target]
YS = YS[target]


target3 = np.where(YNS<499)
YS = YS[target3]
YR = YR[target3]
YNS = YNS[target3]


fig_size = (12, 4)
fig, ax = plt.subplots(1,2,figsize=fig_size)

ax[0].plot(x,y,'r')
ax[0].scatter(YR,YNS)
ax[0].set_xlabel(r"$\mathbf{y}$", fontsize =14)
ax[0].set_ylabel(r"$\mathbf{y}^{\langle 6 \rangle}$", fontsize =14)
ax[0].text(10, 450, r"$R^2 = 0.91$", fontsize=14, ha='left')
ax[0].tick_params(axis='x', labelsize=14)
ax[0].tick_params(axis='y', labelsize=14)

ax[1].plot(x,y,'r')
ax[1].scatter(YR,YS)
ax[1].set_xlabel(r"$\mathbf{y}$", fontsize =14)
ax[1].set_ylabel(r"$\overline{\mathbf{y}^{\langle 6 \rangle}}$", fontsize =14)
ax[1].text(10, 450, r"$R^2 = 0.06$", fontsize=14, ha='left')
ax[1].tick_params(axis='x', labelsize=14)
ax[1].tick_params(axis='y', labelsize=14)


#plt.plot(x,y,'r')
#plt.scatter(YR,YNS)
#plt.ylim((0,500))
#plt.xlim((0,500))
#plt.xlabel(r"$\mathbf{y}$", fontsize =14)
#plt.ylabel(r"$\mathbf{y}^{\langle 6 \rangle}$", fontsize =14)
#plt.text(10, 450, r"$R^2 = 0.91$", fontsize=14, ha='left')
plt.savefig('/home/pgrad1/2712549y/.local/lib/python3.6/site-packages/myokit/plot/repeatabilitytest/apd90/fig080.pdf',bbox_inches='tight')
plt.show()


























