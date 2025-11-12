import numpy as np

arr = [10, 20, 30, 40, 60, 70, 80, 90, 10]
l = len(arr)

# Calculate Median
arr.sort()
if l % 2 == 1:
    med = arr[l // 2]
else:
    med1 = arr[l // 2]
    med2 = arr[(l // 2) - 1]
    med = (med1 + med2) / 2

# Calculate Mean
mean = sum(arr) / l

# Calculate Standard Deviation
sd = np.std(arr)

# Calculate Skewness
sk = 3 * (mean - med) / sd

# Output results
print(f"Median: {med}")
print(f"Mean: {mean}")
print(f"Skewness: {sk}")
