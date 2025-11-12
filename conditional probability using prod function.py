# 1. Define a function to calculate product
def prod(a, b):
    return a * b

# --- PART 1: Weather Experiment ---
rain_status = ["Rain", "No rain", "Rain", "Rain", "No rain"]
sky_status = ["Cloudy", "cloudy", "Clear", "Cloudy", "clear"]

rain_days = 0
cloudy_and_rain_days = 0

for i in range(len(rain_status)):
    if rain_status[i] == "Rain":
        rain_days += 1
        # The code checks if it is NOT Clear (implying it is cloudy)
        if sky_status[i] != "Clear": 
            cloudy_and_rain_days += 1

# Calculate P(Cloudy | Rain)
# using ternary operator to handle division by zero
P_cloudy_given_rain = cloudy_and_rain_days / rain_days if rain_days != 0 else 0

print("Total Rainy days:", rain_days)
print("Cloudy and rainy days:", cloudy_and_rain_days)
print("P(Cloudy | Rain) =", round(P_cloudy_given_rain, 4))


# --- PART 2: Dice Experiment ---
arr = [1, 2, 3, 4, 5, 6]
count_A_and_B = 0
count_B = 0

for i in arr:
    if i > 3:  # Event B
        count_B += 1
        if i % 2 == 0:  # Event A (Even)
            count_A_and_B += 1

total_outcomes = len(arr)
P_B = count_B / total_outcomes
P_A_and_B = count_A_and_B / total_outcomes

# Calculate P(A | B)
if P_B != 0:
    P_A_given_B = P_A_and_B / P_B 
else:
    P_A_given_B = 0

print("P(A|B) =", round(P_A_given_B, 4))


# --- PART 3: Combined Probability ---
combined_probability = prod(P_cloudy_given_rain, P_A_given_B)

print("Combined Probability = P(Cloudy|Rain) * P(A|B)")
print("Combined Probability =", round(combined_probability, 4))
