import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_cleaned.csv')
df['event_time'] = pd.to_datetime(df['event_time'])

purchases = df[df['event_type'] == 'purchase'].copy()

# Revenue by day
daily_revenue = purchases.groupby('date')['price'].sum().reset_index()
daily_revenue.columns = ['date', 'revenue']

# Revenue by category
category_revenue = purchases.groupby('category_code')['price'].sum().sort_values(ascending=False).head(10)

# Revenue by brand
brand_revenue = purchases.groupby('brand')['price'].sum().sort_values(ascending=False).head(10)

print("Top 10 Categories by Revenue:")
print(category_revenue)

print("\nTop 10 Brands by Revenue:")
print(brand_revenue)

# Plot daily revenue
plt.figure(figsize=(14, 5))
plt.plot(daily_revenue['date'], daily_revenue['revenue'], color='blue')
plt.title('Daily Revenue')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('daily_revenue.png')
print("\nChart saved as daily_revenue.png")

# Save summaries
daily_revenue.to_csv('daily_revenue.csv', index=False)
category_revenue.to_csv('category_revenue.csv')
brand_revenue.to_csv('brand_revenue.csv')
print("Revenue data saved to CSV files")
