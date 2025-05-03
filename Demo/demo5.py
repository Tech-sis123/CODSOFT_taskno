import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example: Replace with your actual SAIDI mean values over iterations
mean_saidi_values = [610, 607, 605, 603, 602, 601.5, 601, 600.8, 600.6, 600.5,
                     600.4, 600.3, 600.2, 600.15, 600.1, 600.08, 600.06, 600.05, 600.02, 600.01]

iterations = np.arange(1, len(mean_saidi_values) + 1)

# Smoothing using moving average (window size = 3)
smoothed = pd.Series(mean_saidi_values).rolling(window=3).mean()

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(iterations, mean_saidi_values, label='Original SAIDI Mean', marker='o')
plt.plot(iterations, smoothed, label='Smoothed SAIDI (Moving Avg)', linestyle='--', color='red')
plt.xlabel('Iteration')
plt.ylabel('Estimated SAIDI Mean')
plt.title('Convergence of SAIDI Mean over Iterations')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
