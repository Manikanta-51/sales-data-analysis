import pandas as pd

# Load dataset
data = pd.read_csv("sales.csv")

# Create total column
data["total"] = data["price"] * data["quantity"]

# Total sales
total_sales = data["total"].sum()

# Best selling product
best_product = data.groupby("product")["quantity"].sum().idxmax()

print("Total Sales:", total_sales)
print("Best Selling Product:", best_product)