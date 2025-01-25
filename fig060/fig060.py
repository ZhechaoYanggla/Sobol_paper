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
labels = [r"$\mathbf{y}^{\langle 6 \rangle}$", r"$\mathbf{y}^{\langle 7 \rangle}$", r"$\mathbf{y}^{\langle 8 \rangle}$", 
          r"$\mathbf{y}^{\langle 9 \rangle}$", r"$\mathbf{y}^{\langle 10 \rangle}$", r"$\mathbf{y}^{\langle 11 \rangle}$", 
          r"$\mathbf{y}^{\langle 12 \rangle}$", r"$\mathbf{y}^{\langle 13 \rangle}$", r"$\mathbf{y}^{\langle 14 \rangle}$", r"$\mathbf{y}$"]

# Set up the figure and axis
fig, ax1 = plt.subplots(figsize=(8, 4))

# Plot error data on the first axis
ax1.plot(error, marker='o', color='blue', label='Error')
ax1.tick_params(axis='x', labelsize=14, pad=2)
ax1.tick_params(axis='y', labelsize=14, pad=2)
ax1.set_ylabel('Error', fontsize=14, color='blue')
ax1.xaxis.set_ticks_position('bottom')

# Set up secondary y-axis for Rvalue data
ax2 = ax1.twinx()
ax2.plot(Rvalue, marker='x', linestyle='--', color='green', label=r'$R^2$ Value')  # Updated marker and line style
ax2.set_xticks(np.arange(0, len(error)))  # Set ticks starting from the second position
ax2.set_xticklabels(labels, fontsize=14)  # Bottom labels
ax2.tick_params(axis='y', labelsize=14, pad=2)
ax2.set_ylabel(r'$R^2$ Value', fontsize=14, color='green')  # Updated label to R^2 Value
ax2.xaxis.set_ticks_position('bottom')

# Adjust layout and spacing
plt.tight_layout()
plt.subplots_adjust(top=0.85)  # Ensure the top x-tick has enough room

# Save and display the figure
plt.savefig('fig060.pdf', bbox_inches='tight', pad_inches=0.1)
plt.show()
