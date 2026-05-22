import pandas as pd

df = pd.read_csv('ecommerce_cleaned.csv')

# Count each event type
funnel = df['event_type'].value_counts()
print("Event counts:\n", funnel)

# Funnel drop-off rates
views     = len(df[df['event_type'] == 'view'])
carts     = len(df[df['event_type'] == 'cart'])
purchases = len(df[df['event_type'] == 'purchase'])

print(f"\nViews:     {views}")
print(f"Carts:     {carts}")
print(f"Purchases: {purchases}")

print(f"\nView → Cart conversion:     {round(carts/views*100, 2)}%")
print(f"Cart → Purchase conversion: {round(purchases/carts*100, 2)}%")
print(f"Overall conversion:         {round(purchases/views*100, 2)}%")

# Save funnel summary
funnel_df = pd.DataFrame({
    'Stage': ['View', 'Cart', 'Purchase'],
    'Count': [views, carts, purchases]
})
funnel_df.to_csv('funnel_analysis.csv', index=False)
print("\nFunnel analysis saved to funnel_analysis.csv")
