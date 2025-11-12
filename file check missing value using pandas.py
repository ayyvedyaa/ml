import pandas as pd

# Dataset
data = {
    'First Name': ['Douglas', 'Thomas', 'Jerry', 'Maria', 'Douglas'],
    'Gender': ['Male', 'Male', 'Female', 'Male', 'Female'],
    'Salary': [97308, 118200, 85910, 138705, 130590],
    'Bonus %': [10.389, 6.170, 11.858, 9.360, 11.858],
    'Senior Management': [True, True, False, True, False]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display missing values per column
print("Missing values per column:")
print(df.isnull().sum())

# Fill missing Salary and Bonus values with their mean (if any)
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Bonus %'] = df['Bonus %'].fillna(df['Bonus %'].mean())

# Save cleaned data to CSV
df.to_csv("cleaned_data.csv", index=False)

# Display cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)
