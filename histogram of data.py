import matplotlib.pyplot as plt
data=[10,10,30,40,40,40]
plt.hist(data, bins=5, edgecolor='black')
plt.xlabel('values')
plt.ylabel('frequency')
plt.title('histogram')
plt.show()
