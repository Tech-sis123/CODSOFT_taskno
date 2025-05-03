import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Realistic IEEE-based values
saidi = [120, 143, 95, 193, 170, 134, 158, 111, 143]
saifi = [1.1, 1.3, 0.9, 1.2, 1.5, 1.1, 1.0, 0.8, 1.3]
caidi = [round(s / f, 2) for s, f in zip(saidi, saifi)]

def plot_distribution(data, label, color):
    mu, std = norm.fit(data)
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=6, density=True, alpha=0.6, color=color, edgecolor='black', label='Histogram')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'r', linewidth=2, label=f'Normal Fit\nμ={mu:.2f}, σ={std:.2f}')
    plt.title(f'{label} - Histogram with Normal Distribution Fit')
    plt.xlabel(label)
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plot each separately
plot_distribution(saidi, 'SAIDI (minutes)', 'skyblue')
plot_distribution(saifi, 'SAIFI (interruptions)', 'lightgreen')
plot_distribution(caidi, 'CAIDI (minutes)', 'salmon')
