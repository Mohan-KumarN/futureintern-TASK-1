import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

# Parameters
num_rows = 1000
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

# Categories and Products
categories = {
    'Electronics': ['Smartphone', 'Laptop', 'Headphones', 'Tablet', 'Smartwatch'],
    'Furniture': ['Chair', 'Desk', 'Sofa', 'Bookshelf', 'Lamp'],
    'Office Supplies': ['Paper', 'Binder', 'Pen', 'Folder', 'Stapler'],
    'Clothing': ['T-shirt', 'Jeans', 'Jacket', 'Sneakers', 'Hat']
}

regions = ['North', 'South', 'East', 'West', 'Central']

# Generate data
data = []
for _ in range(num_rows):
    category = np.random.choice(list(categories.keys()))
    product = np.random.choice(categories[category])
    region = np.random.choice(regions)
    date = start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days))
    
    # Random sales and quantity
    quantity = np.random.randint(1, 11)
    if category == 'Electronics':
        price = np.random.uniform(50, 1500)
    elif category == 'Furniture':
        price = np.random.uniform(30, 800)
    elif category == 'Office Supplies':
        price = np.random.uniform(5, 100)
    else: # Clothing
        price = np.random.uniform(10, 200)
    
    sales = round(price * quantity, 2)
    profit_margin = np.random.uniform(0.1, 0.4)
    profit = round(sales * profit_margin, 2)
    
    data.append([date, product, category, region, sales, quantity, profit])

# Create DataFrame
df = pd.DataFrame(data, columns=['Date', 'Product', 'Category', 'Region', 'Sales', 'Quantity', 'Profit'])

# Save to CSV
df.to_csv('sales_data.csv', index=False)
print("Synthetic sales data generated successfully: sales_data.csv")
