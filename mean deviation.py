import numpy as np
data=[10,20,30,40,50]
mean_dev=np.mean(np.abs(data-np.mean(data)))
print("mean dev is", mean_dev)
#Mean deviation is a measure of how spread out a set of data is.
