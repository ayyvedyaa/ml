# Data: A standard 6-sided die
arr = [1, 2, 3, 4, 5, 6]

count_A_and_B = 0
count_B = 0

for i in arr:
    # Event B: The number is greater than 3
    if i > 3:
        count_B += 1
        
        # Event A: The number is even (i % 2 == 0)
        # This is nested, so it counts items that are BOTH > 3 AND Even
        if i % 2 == 0:
            count_A_and_B += 1

total_outcomes = len(arr)

# Calculate Probabilities
P_B = count_B / total_outcomes
P_A_and_B = count_A_and_B / total_outcomes

# Calculate Conditional Probability P(A|B) = P(A n B) / P(B)
if P_B != 0:
    P_A_given_B = P_A_and_B / P_B
else:
    P_A_given_B = 0

print("P(A|B) =", round(P_A_given_B, 4))
