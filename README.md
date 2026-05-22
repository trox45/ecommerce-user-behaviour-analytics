# E-Commerce User Behaviour Analytics

## Project Overview
This project analyzes user behaviour data from an e-commerce platform using Python and Power BI. The dataset contains 500,000+ events including views, cart additions, and purchases from October 2019.

## Tools & Technologies
- **Python** — Data cleaning and analysis
- **Pandas** — Data manipulation
- **Matplotlib** — Data visualization
- **Power BI** — Interactive dashboard

## Dataset
- Source: [Kaggle — E-Commerce Behavior Data](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)
- Size: 500,000 rows (sample from 2019-Oct.csv)
- Features: event_time, event_type, product_id, category_code, brand, price, user_id

## Project Steps

### 1. Data Cleaning (`step3_load_clean.py`)
- Loaded 500,000 rows from raw CSV
- Dropped null values
- Parsed datetime columns
- Removed duplicate events
- Saved cleaned data to `ecommerce_cleaned.csv`

### 2. Funnel Analysis (`step4_funnel.py`)
- Calculated conversion rates across the buyer journey
- View → Cart → Purchase funnel
- **Results:** 300K views → 7K carts → 7K purchases (2.4% overall conversion)

### 3. RFM Segmentation (`step5_rfm.py`)
- Segmented customers based on Recency, Frequency, and Monetary value
- Segments: Champion, Loyal, Potential, At Risk, Lost
- **Results:** ~50% Champions, ~50% Loyal customers

### 4. Revenue Analysis (`step6_revenue.py`)
- Daily revenue trends
- Top 10 categories by revenue
- Top 10 brands by revenue
- **Results:** $2.78M total revenue, Apple & Samsung lead brands, Electronics dominates

## Power BI Dashboard
The dashboard contains 3 pages:
- **Page 1:** User Conversion Funnel
- **Page 2:** Customer RFM Segments
- **Page 3:** Revenue by Category and Brand

## Key Insights
- Only 2.4% of viewers make a purchase — opportunity to improve cart conversion
- Electronics (especially smartphones) account for the majority of revenue
- Apple alone generates over $1.5M in revenue
- Most customers are either Champions or Loyal — strong repeat buyer base

## Files
| File | Description |
|------|-------------|
| `step3_load_clean.py` | Data cleaning script |
| `step4_funnel.py` | Funnel analysis script |
| `step5_rfm.py` | RFM segmentation script |
| `step6_revenue.py` | Revenue analysis script |
| `ecommerce_dashboard.pbix` | Power BI dashboard |
| `daily_revenue.png` | Daily revenue chart |

## Author
Twisha Salunke — Data Analyst
