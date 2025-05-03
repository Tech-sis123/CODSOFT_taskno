import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define SAIDI and SAIFI values
saidi_values = [
    613, 576, 622, 582, 585, 564, 583, 614, 563, 591, 599, 563,
    625, 621, 582, 594, 619, 583, 610, 620, 603, 621, 576, 623,
    623, 608, 623, 612, 616, 625, 564, 612
]

saifi_values = [
    34, 32, 28, 34, 29, 31, 28, 31, 33, 29, 29, 28,
    29, 32, 29, 31, 31, 34, 31, 34, 31, 32, 35, 34,
    30, 33, 28, 31, 29, 35, 31, 29
]

# Calculate CAIDI (SAIDI / SAIFI)
caidi_values = [round(saidi / saifi, 2) for saidi, saifi in zip(saidi_values, saifi_values)]

# Convert to NumPy arrays
saidi_array = np.array(saidi_values)
saifi_array = np.array(saifi_values)
caidi_array = np.array(caidi_values)

# Function to plot histogram and normal curve
def plot_histogram_with_fit(data, title, color):
    mu, std = norm.fit(data)
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=10, density=True, alpha=0.6, color=color, edgecolor='black', label='Histogram')
    x = np.linspace(min(data), max(data), 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'r', linewidth=2, label=f'Normal Fit\nμ={mu:.2f}, σ={std:.2f}')
    plt.title(f'{title} - Histogram and Normal Distribution Fit (MLE)')
    plt.xlabel(title)
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plot for each metric
# plot_histogram_with_fit(saidi_array, 'SAIDI', 'skyblue')
plot_histogram_with_fit(saifi_array, 'SAIFI', 'lightgreen')
plot_histogram_with_fit(caidi_array, 'CAIDI', 'lightcoral')

