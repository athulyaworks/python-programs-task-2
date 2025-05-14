import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create sample data
np.random.seed(42)  # For reproducible results

# Generate sample sales data
dates = [datetime.now() - timedelta(days=x) for x in range(100, 0, -1)]
products = ['Product A', 'Product B', 'Product C', 'Product D']
salespersons = ['John', 'Jane', 'Bob', 'Alice', 'Charlie']

data = []
for date in dates:
    n_records = np.random.randint(1, 5)  # 1-4 records per day
    for _ in range(n_records):
        record = {
            'Date': date.strftime('%Y-%m-%d'),
            'Product': np.random.choice(products),
            'Salesperson': np.random.choice(salespersons),
            'Quantity': np.random.randint(1, 20),
            'Unit_Price': np.random.uniform(10, 100),
            'Region': np.random.choice(['North', 'South', 'East', 'West'])
        }
        record['Total_Revenue'] = record['Quantity'] * record['Unit_Price']
        data.append(record)

# Create DataFrame
df = pd.DataFrame(data)

# Create Excel file with multiple sheets
with pd.ExcelWriter('sales_data.xlsx', engine='xlsxwriter') as writer:
    # Write raw data
    df.to_excel(writer, sheet_name='Raw Data', index=False)
    
    # Create summaries
    # 1. Summary by Product
    product_summary = df.groupby('Product').agg({
        'Quantity': 'sum',
        'Total_Revenue': ['sum', 'mean', 'count']
    }).round(2)
    product_summary.to_excel(writer, sheet_name='Product Summary')
    
    # 2. Summary by Salesperson
    sales_summary = df.groupby('Salesperson').agg({
        'Quantity': 'sum',
        'Total_Revenue': ['sum', 'mean', 'count']
    }).round(2)
    sales_summary.to_excel(writer, sheet_name='Salesperson Summary')
    
    # 3. Summary by Region
    region_summary = df.groupby('Region').agg({
        'Quantity': 'sum',
        'Total_Revenue': ['sum', 'mean', 'count']
    }).round(2)
    region_summary.to_excel(writer, sheet_name='Region Summary')
    
    # 4. Monthly Summary
    df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M')
    monthly_summary = df.groupby('Month').agg({
        'Quantity': 'sum',
        'Total_Revenue': ['sum', 'mean', 'count']
    }).round(2)
    monthly_summary.to_excel(writer, sheet_name='Monthly Summary')

print("Excel file 'sales_data.xlsx' created successfully!")

# Read the Excel file back and display summaries
print("\n" + "="*50)
print("DATA SUMMARIES")
print("="*50)

# Read the Excel file
df_read = pd.read_excel('sales_data.xlsx', sheet_name='Raw Data')

# Overall Statistics
print("\n1. OVERALL STATISTICS")
print("-" * 30)
print(f"Total Records: {len(df_read)}")
print(f"Date Range: {df_read['Date'].min()} to {df_read['Date'].max()}")
print(f"Total Revenue: ${df_read['Total_Revenue'].sum():,.2f}")
print(f"Average Revenue per Sale: ${df_read['Total_Revenue'].mean():.2f}")
print(f"Total Quantity Sold: {df_read['Quantity'].sum()}")

# Top Products
print("\n2. TOP 3 PRODUCTS BY REVENUE")
print("-" * 30)
top_products = df_read.groupby('Product')['Total_Revenue'].sum().sort_values(ascending=False).head(3)
for product, revenue in top_products.items():
    print(f"{product}: ${revenue:,.2f}")

# Top Salespersons
print("\n3. TOP 3 SALESPERSONS BY REVENUE")
print("-" * 30)
top_sales = df_read.groupby('Salesperson')['Total_Revenue'].sum().sort_values(ascending=False).head(3)
for person, revenue in top_sales.items():
    print(f"{person}: ${revenue:,.2f}")

# Regional Performance
print("\n4. REVENUE BY REGION")
print("-" * 30)
region_revenue = df_read.groupby('Region')['Total_Revenue'].sum().sort_values(ascending=False)
for region, revenue in region_revenue.items():
    print(f"{region}: ${revenue:,.2f}")

# Daily Average
print("\n5. DAILY PERFORMANCE")
print("-" * 30)
daily_stats = df_read.groupby('Date')['Total_Revenue'].sum()
print(f"Average Daily Revenue: ${daily_stats.mean():.2f}")
print(f"Best Day: {daily_stats.idxmax()} (${daily_stats.max():.2f})")
print(f"Worst Day: {daily_stats.idxmin()} (${daily_stats.min():.2f})")

# Basic descriptive statistics
print("\n6. DESCRIPTIVE STATISTICS")
print("-" * 30)
print(df_read[['Quantity', 'Unit_Price', 'Total_Revenue']].describe())

print("\n" + "="*50)
print("Analysis complete! Check 'sales_data.xlsx' for detailed data and summaries.")
print("="*50)