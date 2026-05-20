import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create a directory for assets if it doesn't exist
if not os.path.exists('assets'):
    os.makedirs('assets')

# Load the data
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 1. Data Cleaning
# Check for missing values
print("Missing values:\n", df.isnull().sum())

# 2. Revenue Trends
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['Month'].astype(str)

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Sales', marker='o')
plt.title('Monthly Revenue Trends (2025)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('assets/revenue_trends.png')
plt.close()

# 3. Top-selling Products (by Sales)
top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=top_products, x='Sales', y='Product', palette='viridis')
plt.title('Top 10 Products by Revenue')
plt.tight_layout()
plt.savefig('assets/top_products.png')
plt.close()

# 4. High-value Categories
category_performance = df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

plt.figure(figsize=(8, 8))
plt.pie(category_performance['Sales'], labels=category_performance['Category'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Revenue Distribution by Category')
plt.savefig('assets/category_revenue.png')
plt.close()

# 5. Regional Performance
regional_performance = df.groupby('Region')['Sales'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=regional_performance, x='Region', y='Sales', palette='magma')
plt.title('Revenue by Region')
plt.tight_layout()
plt.savefig('assets/regional_performance.png')
plt.close()

# 6. Profit Analysis
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=category_profit, x='Profit', y='Category', palette='coolwarm')
plt.title('Total Profit by Category')
plt.tight_layout()
plt.savefig('assets/category_profit.png')
plt.close()

print("Analysis complete. Visualizations saved in 'assets/' folder.")

# Generate summary stats for the report
summary_stats = {
    'Total Revenue': df['Sales'].sum(),
    'Total Profit': df['Profit'].sum(),
    'Total Units Sold': df['Quantity'].sum(),
    'Avg Order Value': df['Sales'].mean(),
    'Top Category': category_performance.loc[category_performance['Sales'].idxmax(), 'Category'],
    'Top Region': regional_performance.loc[regional_performance['Sales'].idxmax(), 'Region']
}

print("\n--- Summary Statistics ---")
for key, value in summary_stats.items():
    if isinstance(value, float):
        print(f"{key}: ${value:,.2f}")
    else:
        print(f"{key}: {value}")
