# Data setup
# Note: I filled in the list values based on the logic required to get your output
rain_status = ["rain", "no rain", "rain", "rain", "no rain"]
sky_status = ["cloudy", "cloudy", "clear", "cloudy", "clear"]

rain_days = 0
cloudy_rain_days = 0

# Loop through the data
for i in range(len(rain_status)):
    # Check if it rained
    if rain_status[i] == "rain":
        rain_days += 1
        
        # Check if it was ALSO cloudy (Nested inside the rain check)
        if sky_status[i] == "cloudy":
            cloudy_rain_days += 1

# Calculate Conditional Probability: P(Cloudy | Rain)
# Using a ternary operator to avoid division by zero error
P_cloudy_given_rain = cloudy_rain_days / rain_days if rain_days != 0 else 0

# Output
print("Total rainy days:", rain_days)
print("Cloudy and rainy days:", cloudy_rain_days)
print("P(Cloudy | Rain):", round(P_cloudy_given_rain, 4))
