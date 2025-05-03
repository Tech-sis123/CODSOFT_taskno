import numpy as np
import matplotlib.pyplot as plt

# Use your latest SAIDI and SAIFI values
saidi_values = np.array([
    613, 576, 622, 582, 585, 564, 583, 614, 563, 591, 599, 563,
    625, 621, 582, 594, 619, 583, 610, 620, 603, 621, 576, 623,
    623, 608, 623, 612, 616, 625, 564, 612
])

saifi_values = np.array([
    34, 32, 28, 34, 29, 31, 28, 31, 33, 29, 29, 28,
    29, 32, 29, 31, 31, 34, 31, 34, 31, 32, 35, 34,
    30, 33, 28, 31, 29, 35, 31, 29
])

# Calculate CAIDI
caidi_values = saidi_values / saifi_values

# Function to calculate running mean (MLE estimate at each step)
def running_mean(data):
    return np.cumsum(data) / np.arange(1, len(data)+1)

# Compute running MLEs
running_mle_saidi = running_mean(saidi_values)
running_mle_saifi = running_mean(saifi_values)
running_mle_caidi = running_mean(caidi_values)

# Plot for SAIDI
plt.figure(figsize=(10, 5))
plt.plot(running_mle_saidi, marker='o', color='skyblue', label='SAIDI MLE (Running Mean)')
plt.title("MLE Estimation Over Iterations - SAIDI")
plt.xlabel("Iteration")
plt.ylabel("Mean SAIDI")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot for SAIFI
plt.figure(figsize=(10, 5))
plt.plot(running_mle_saifi, marker='o', color='lightgreen', label='SAIFI MLE (Running Mean)')
plt.title("MLE Estimation Over Iterations - SAIFI")
plt.xlabel("Iteration")
plt.ylabel("Mean SAIFI")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot for CAIDI
plt.figure(figsize=(10, 5))
plt.plot(running_mle_caidi, marker='o', color='salmon', label='CAIDI MLE (Running Mean)')
plt.title("MLE Estimation Over Iterations - CAIDI")
plt.xlabel("Iteration")
plt.ylabel("Mean CAIDI")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
