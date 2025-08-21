import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([10, 20, 30, 40])
y = np.array([15, 25, 35, 45])
sizes = np.array([100, 300, 200, 400])  # Bubble sizes

plt.scatter(x, y, s=sizes, alpha=0.5, c='darkblue', edgecolors='red')

plt.title("Bubble Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()