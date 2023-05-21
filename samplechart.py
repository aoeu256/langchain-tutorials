import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.random.randint(low=1, high=11, size=50)

# Plot the data
plt.bar(range(len(x)), x)
plt.show()