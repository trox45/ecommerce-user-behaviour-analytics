import pandas as pd

df = pd.read_csv('ecommerce_cleaned.csv')
df['event_time'] = pd.to_datetime(df['event_time'])

# Keep only purchases
purchases = df[df['event_type'] == 'purchase'].copy()

# Reference date
ref_date = purchases['event_time'].max()

# Calculate RFM
rfm = purchases.groupby('user_id').agg(
    Recency   = ('event_time', lambda x: (ref_date - x.max()).days),
    Frequency = ('event_type', 'count'),
    Monetary  = ('price', 'sum')
).reset_index()

print("RFM Table Sample:")
print(rfm.head(10))

# Simple scoring based on median
rfm['R_Score'] = (rfm['Recency']   <= rfm['Recency'].median()).astype(int) + 1
rfm['F_Score'] = (rfm['Frequency'] >= rfm['Frequency'].median()).astype(int) + 1
rfm['M_Score'] = (rfm['Monetary']  >= rfm['Monetary'].median()).astype(int) + 1

# Segment users
def segment(row):
    r = int(row['R_Score'])
    f = int(row['F_Score'])
    m = int(row['M_Score'])
    if r == 2 and f == 2 and m == 2:
        return 'Champion'
    elif r == 2 and f == 2:
        return 'Loyal'
    elif r == 2 and f == 1:
        return 'Potential'
    elif r == 1 and f == 2:
        return 'At Risk'
    else:
        return 'Lost'

rfm['Segment'] = rfm.apply(segment, axis=1)

print("\nSegment counts:")
print(rfm['Segment'].value_counts())

print("\nRFM Summary:")
print(rfm.groupby('Segment')[['Recency','Frequency','Monetary']].mean().round(2))

rfm.to_csv('rfm_segments.csv', index=False)
print("\nRFM data saved to rfm_segments.csv")
