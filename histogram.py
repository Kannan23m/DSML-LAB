import matplotlib.pyplot as plt

data = [12, 15, 12, 18, 19, 15, 14, 20, 22, 21, 15, 18, 16]

plt.hist(data, bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
