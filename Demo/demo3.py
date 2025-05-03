import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Selected 9 values (from 33) based on random.seed(42)
saidi_values = [603, 582, 582, 616, 625, 564, 612, 583, 608]
saifi_values = [31, 34, 29, 29, 35, 31, 29, 28, 33]
caidi_values = [round(saidi / saifi, 2) for saidi, saifi in zip(saidi_values, saifi_values)]

# Create DataFrame
data = pd.DataFrame({
    'SAIDI': saidi_values,
    'SAIFI': saifi_values,
    'CAIDI': caidi_values
})

# Display correlation matrix
print("Correlation Matrix:")
print(data.corr())

# MLE and Plotting for each variable
for column in data.columns:
    values = data[column].values
    mu, std = norm.fit(values)

    plt.figure(figsize=(8, 5))
    plt.hist(values, bins=6, density=True, alpha=0.6, color='skyblue', edgecolor='black', label=f'{column} Histogram')

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'r', linewidth=2, label=f'Normal Dist.\nμ={mu:.2f}, σ={std:.2f}')

    plt.title(f'{column} - Histogram and Normal Distribution Fit (MLE)')
    plt.xlabel(column)
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
