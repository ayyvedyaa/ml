import pandas as pd

# Read CSV file
df = pd.read_csv('employees.csv')
print(df)

# Add a new column "City"
df = pd.read_csv('employees.csv')
df['City'] = ['New York', 'Los Angeles', 'Chicago', 'San Francisco']
df.to_csv('employees.csv', index=False)
print(df)

# Multiply Salary by 2
df = pd.read_csv('employees.csv')
df['Salary'] *= 2
df.to_csv('employees.csv', index=False)
print(df)

# Drop the "City" column
df = pd.read_csv('employees.csv')
df.drop('City', axis=1, inplace=True)
df.to_csv('employees.csv', index=False)
print(df)
