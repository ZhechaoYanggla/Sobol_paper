import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.4

# Define the data arrays
barsapd30 = np.array([0.298551, 0.489548, 0.253750, 0.322475, 0.446554, 0.819785, 0.337626, 0.340235, 0.269617, 0.186696, 0.242554, 0.128651, 0.117747, 0.198473, 0.201128])
barsapd90 = np.array([0.063756, 0.343800, 0.045965, 0.171277, 0.238207, 0.543686, 0.093728, 0.078175, 0.050839, 0.029096, 0.052875, 0.009201, 0.014913, 0.022159, 0.033559])
barsB = np.array([0.080936, 0.257172, 0.086599, 0.126789, 0.235577, 0.721407, 0.159594, 0.179478, 0.059436, 0.034067, 0.088262, 0.012136, 0.014043, 0.028355, 0.038835])
barsVplt = np.array([0.088029, 0.263078, 0.128642, 0.350030, 0.149469, 0.407008, 0.258628, 0.081045,  0.093353, 0.052513, 0.121782, 0.020484, 0.043503, 0.053569, 0.064066])
barsvmax = np.array([0.062823, 0.125859, 0.125020, 0.135640, 0.075471, 0.438057, 0.400387, 0.125954, 0.065601, 0.043258, 0.090624, 0.022982, 0.045073, 0.035607, 0.100303])
barsvrest = np.array([0.162326, 0.543376, 0.106973, 0.469340, 0.272863, 0.546389, 0.194061, 0.301515, 0.131321, 0.091091, 0.106615, 0.039087, 0.050379, 0.071073, 0.090155])

# Calculate grand total
bargrand = barsapd30 + barsapd90 + barsB + barsVplt + barsvmax + barsvrest

# X-axis labels
labels = [r'$p_{\text{NaK}}$', r'$p_{\text{Kr}}$',r'$p_{\text{tos}}$', r'$p_{\text{K1}}$', r'$p_{\text{NaCa}}$', r'$p_{\text{Clb}}$', r'$p_{\text{CaL}}$', r'$p_{\text{Ks}}$', r'$p_{\text{Cab}}$', r'$p_{\text{Cap}}$', r'$p_{\text{ClCa}}$',r'$p_{\text{Kp}}$', r'$p_{\text{Na}}$', r'$p_{\text{Nab}}$', r'$p_{\text{tof}}$']

# Sort bargrand and labels in decreasing order
sorted_indices = np.argsort(bargrand)[::-1]
bargrand_sorted = bargrand[sorted_indices]
labels_sorted = np.array(labels)[sorted_indices]

# Plotting
plt.figure(figsize=(10, 4), dpi=80)
plt.bar(np.arange(len(bargrand_sorted)), bargrand_sorted, width=barWidth, color='orangered', edgecolor='white')
plt.xticks(np.arange(len(bargrand_sorted)), labels_sorted, fontsize=12)

plt.tick_params(axis='x', labelsize=12, pad=2)
plt.tick_params(axis='y', labelsize=12, pad=2)
plt.ylabel('Grand total Sobol sensitivity index', fontsize=12)

# Save the plot as a PDF file
plt.savefig('grand_total_sorted.pdf', bbox_inches='tight', pad_inches=0.1)
plt.show()
