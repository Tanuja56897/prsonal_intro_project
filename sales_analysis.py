import pandas as pd

# Load sales dataset
data = pd.read_csv("sales.csv")

print("Original Data:\n")
print(data)

# ---------------------------
# Basic Information
# ---------------------------
print("\nNumber of rows and columns:", data.shape)
print("\nColumn Names:", data.columns)
print("\nData Info:")
print(data.info())

# ---------------------------
# Handle Missing Values
# ---------------------------
data['Quantity'].fillna(data['Quantity'].mean(), inplace=True)
data['Price'].fillna(data['Price'].mean(), inplace=True)

print("\nAfter Filling Missing Values:\n")
print(data)

# ---------------------------
# Calculate Total Sales
# ---------------------------
data['Total_Sales'] = data['Quantity'] * data['Price']

# ---------------------------
# Calculate Metrics
# ---------------------------
total_revenue = data['Total_Sales'].sum()
average_sales = data['Total_Sales'].mean()
highest_sales = data['Total_Sales'].max()

best_product = data.groupby('Product')['Total_Sales'].sum().idxmax()

print("\nTotal Revenue:", total_revenue)
print("Average Sales:", average_sales)
print("Highest Sales:", highest_sales)
print("Best Selling Product:", best_product)

print("\nProject Completed Successfully!")