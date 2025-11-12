import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

np.random.seed(0)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

model = LinearRegression()
model.fit(x, y)

x_new = np.linspace(0, 2, 100).reshape(100, 1)
y_predict = model.predict(x_new)

plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x_new, y_predict, color='red', label='Regression line')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression")
plt.legend()
plt.show()
