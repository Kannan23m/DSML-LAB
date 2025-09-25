import numpy as np

data = [5, 7, 8, 2, 17, 2, 9, 4, 11]

# Compute quantiles (25%, 50%, 75%)
quantiles = np.quantile(data, [0.25, 0.5, 0.75])
print(quantiles)
