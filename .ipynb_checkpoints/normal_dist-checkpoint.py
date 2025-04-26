import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Generate synthetic data for student scores
np.random.seed(42)
scores = np.random.normal(loc=70, scale=10, size=1000)  # mean=70, std=10, 1000 samples

# Plot histogram with normal distribution curve
plt.figure(figsize=(10, 5))
sns.histplot(scores, bins=30, kde=True, stat="density", color="skyblue", label="Histogram")

# Overlay the normal distribution curve
x = np.linspace(min(scores), max(scores), 100)
plt.plot(x, norm.pdf(x, np.mean(scores), np.std(scores)), color='red', label="Normal Distribution Curve")

plt.xlabel("Scores")
plt.ylabel("Density")
plt.title("Normal Distribution of Student Scores")
plt.legend()
plt.show()
