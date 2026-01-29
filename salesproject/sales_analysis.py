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
# Convert columns to numeric safely
# ---------------------------
data['Quantity'] = pd.to_numeric(data['Quantity'], errors='coerce')
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')
data['Total_Sales'] = pd.to_numeric(data['Total_Sales'], errors='coerce')

# ---------------------------
# Handle Missing Values
# ---------------------------
data['Quantity'] = data['Quantity'].fillna(data['Quantity'].mean())
data['Price'] = data['Price'].fillna(data['Price'].mean())
data['Total_Sales'] = data['Total_Sales'].fillna(data['Total_Sales'].mean())

print("\nAfter Cleaning Data:\n")
print(data)

# ---------------------------
# Calculate Metrics
# ---------------------------
total_revenue = data['Total_Sales'].sum()
average_sales = data['Total_Sales'].mean()
highest_sales = data['Total_Sales'].max()

best_product = data.groupby('Product')['Total_Sales'].sum().idxmax()

print("\nTotal Revenue:", round(total_revenue, 2))
print("Average Sales:", round(average_sales, 2))
print("Highest Sales:", round(highest_sales, 2))
print("Best Selling Product:", best_product)

print("\nProject Completed Successfully!")