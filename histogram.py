import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
plt.hist(y, bins=4, edgecolor='black')

plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
