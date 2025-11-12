import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd


iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)


df.hist(figsize=(10, 8), bins=20)
plt.suptitle("Histogram of Iris Features")
plt.show()


plt.scatter(df["sepal length (cm)"], df["petal length (cm)"], c=iris.target)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Sepal Length vs Petal Length")
plt.show()
