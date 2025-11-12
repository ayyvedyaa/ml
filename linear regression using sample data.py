import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([[4], [8], [16], [32]])
y = np.array([30000, 45000, 70000, 120000])

model = LinearRegression()
model.fit(x, y)

x_new = np.linspace(1, 32, 100).reshape(-1, 1)
y_predict = model.predict(x_new)

plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x_new, y_predict, color='red', label='Regression line')

plt.xlabel("RAM size")
plt.ylabel("Laptop price")
plt.title("Laptop price using linear regression")
plt.legend()
plt.show()
