import numpy as np
import matplotlib.pyplot as plt

# Data for error and Rvalue
Rvalue = np.array([0.4369555836279964, 0.5099571716456495, 0.5132538668002712, 0.6889962316837188, 
                   0.7447946149813967, 0.7482705366794922, 0.7638309212533065, 0.8348135066537555, 
                   0.8521743543736888, 1])
error = np.array([0.8927655264359381, 0.8562430263376127, 0.7868138363516786, 0.4563855263525482, 
                  0.31461143922299173, 0.19596459024565618, 0.17802349605085177, 0.11314119008629923, 
                  0.08266673770838164, 0])

# Set of labels for x-ticks, starting from the second label
labels = [r'+$p_{\text{NaK}}$', r'+$p_{\text{tos}}$', r'+$p_{\text{ClCa}}$', 
          r'+$p_{\text{Cab}}$', r'+$p_{\text{tof}}$', r'+$p_{\text{Cap}}$', 
          r'+$p_{\text{Nab}}$', r'+$p_{\text{Na}}$', r'+$p_{\text{Kp}}$']

# Add the first label as the title of the entire figure
label1 = [r'$p_{\text{Clb}} + p_{\text{Kr}} + p_{\text{K1}} + p_{\text{CaL}} + p_{\text{NaCa}} + p_{\text{Ks}}$']

# Set up the figure and axis
fig, ax1 = plt.subplots(figsize=(8, 4))
plt.title(r'$p_{\text{Clb}} + p_{\text{Kr}} + p_{\text{K1}} + p_{\text{CaL}} + p_{\text{NaCa}} + p_{\text{Ks}}$', loc = 'left')
# Plot error data on the first axis
ax1.plot(error, marker='o', color='blue', label='Error')
ax1.set_xticks([0])  # Only one tick for the first label on the top
ax1.tick_params(axis='x', labelsize=12, pad=2)
ax1.tick_params(axis='y', labelsize=12, pad=2)
ax1.set_ylabel('Error', fontsize=12, color='blue')
ax1.xaxis.set_ticks_position('bottom')  # Position first label at the top
ax1.set_xticklabels(label1, fontsize=12)

# Set up secondary y-axis for Rvalue data
ax2 = ax1.twinx()
ax2.plot(Rvalue, marker='o', color='green', label='R Value')
ax2.set_xticks(np.arange(1, len(error)))  # Set ticks starting from the second position
ax2.set_xticklabels(labels, fontsize=12)  # Bottom labels
ax2.tick_params(axis='y', labelsize=12, pad=2)
ax2.set_ylabel('R Value', fontsize=12, color='green')
ax2.xaxis.set_ticks_position('bottom')  # Position remaining labels at the bottom

# Adjust layout and spacing
plt.tight_layout()
plt.subplots_adjust(top=0.85)  # Ensure the top x-tick has enough room

# Save and display the figure
plt.savefig('combined_figure.pdf', bbox_inches='tight', pad_inches=0.1)
plt.show()
