import numpy as np

# Generate some random data
np.random.seed(0)
data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], size=100)

from scipy.stats import gaussian_kde

kde = gaussian_kde(data.T)
kde.evaluate([0, 0])

from scipy.misc import derivative

# Differentiate the KDE with respect to the first dimension at the point (0, 0)
dx = derivative(lambda x: kde.evaluate([x, 5])[0], 9, dx=1e-6)

# Differentiate the KDE with respect to the second dimension at the point (0, 0)
dy = derivative(lambda x:kde.evaluate([4, x])[0], 7, dx=1e-6)
