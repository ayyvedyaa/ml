import pandas as pd

numbers = [1, 4, 4, 5, 6, 7, 7, 9, 3]

# 1. Calculate Frequency
# value_counts() counts occurances
# sort_index() sorts the data by the number itself (1, 3, 4...) rather than the count
freq = pd.Series(numbers).value_counts().sort_index()

print("--- Frequency ---")
print(freq)

# 2. Calculate Cumulative Frequency
# cumsum() is the "Cumulative Sum" function
cum_freq = freq.cumsum()

print("\n--- Cumulative Frequency ---")
print(cum_freq)

# 3. Calculate Relative Frequency
# NOTE: The formula in the notebook (cum_freq / cum_freq.sum()) is mathematically unusual.
# Standard Relative Frequency is: (Frequency / Total Count)
total_count = freq.sum()
rel_freq = freq / total_count

print("\n--- Relative Frequency ---")
print(rel_freq)
