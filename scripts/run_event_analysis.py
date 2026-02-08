
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import timedelta
import os

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def run_analysis():
    print("Loading data...")
    events_df = pd.read_csv('../data/events/geopolitical_events.csv')
    events_df['Date'] = pd.to_datetime(events_df['Date'], format='mixed', dayfirst=True)

    cp_summary = pd.read_csv('../data/processed/change_point_summary.csv', index_col=0)

    price_df = pd.read_csv('../data/raw/BrentOilPrices.csv')
    price_df['Date'] = pd.to_datetime(price_df['Date'], format='mixed', dayfirst=True)
    price_df = price_df.sort_values('Date').reset_index(drop=True)
    price_df_recent = price_df[price_df['Date'] >= '2012-01-01'].copy().reset_index(drop=True)

    # Extract Change Point Info
    tau_mean = cp_summary.loc['tau', 'mean']
    tau_hdi_3 = cp_summary.loc['tau', 'hdi_3%']
    tau_hdi_97 = cp_summary.loc['tau', 'hdi_97%']

    # Map index to date
    def get_date_from_index(idx, dates):
        idx = int(idx)
        if 0 <= idx < len(dates):
            return dates[idx]
        return None

    cp_date = get_date_from_index(tau_mean, price_df_recent['Date'])
    cp_lower = get_date_from_index(tau_hdi_3, price_df_recent['Date'])
    cp_upper = get_date_from_index(tau_hdi_97, price_df_recent['Date'])

    print(f"Change Point Date: {cp_date}")
    
    # Filter events
    window_days = 90
    nearby_events = events_df[
        (events_df['Date'] >= cp_date - timedelta(days=window_days)) &
        (events_df['Date'] <= cp_date + timedelta(days=window_days))
    ].copy()

    nearby_events['Lag_Days'] = (cp_date - nearby_events['Date']).dt.days
    
    # Visualization
    print("Generating visualization...")
    plt.figure(figsize=(15, 8))

    mask = (price_df_recent['Date'] >= cp_date - timedelta(days=365)) & (price_df_recent['Date'] <= cp_date + timedelta(days=365))
    subset = price_df_recent[mask]

    plt.plot(subset['Date'], subset['Price'], label='Brent Price', color='blue', alpha=0.6)

    plt.axvline(cp_date, color='red', linestyle='--', label=f'Detected Change Point ({cp_date.date()})')
    if cp_lower and cp_upper:
        plt.axvspan(cp_lower, cp_upper, color='red', alpha=0.1, label='Uncertainty (HDI)')

    for _, row in nearby_events.iterrows():
        plt.axvline(row['Date'], color='green', linestyle=':', alpha=0.8)
        plt.text(row['Date'], subset['Price'].max(), row['Event'], rotation=90, verticalalignment='top')

    plt.title('Brent Oil Price: Change Points vs Geopolitical Events')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.tight_layout()
    
    os.makedirs('../results/figures', exist_ok=True)
    plt.savefig('../results/figures/event_association.png')
    print("Figure saved to ../results/figures/event_association.png")

    # Impact statements
    mu_before = cp_summary.loc['mu_before', 'mean']
    mu_after = cp_summary.loc['mu_after', 'mean']
    
    print("\nImpact Analysis Report:")
    print("-" * 30)
    for _, row in nearby_events.iterrows():
        lag = row['Lag_Days']
        lag_desc = "after" if lag < 0 else "before" # Corrected logic: Lag = CP - Event. If CP > Event (positive), Event is before.
        abs_lag = abs(lag)
        
        statement = (
            f"Event: {row['Event']} on {row['Date'].date()}\n"
            f"Change Point Detected: {cp_date.date()} ({abs_lag} days {lag_desc} event)\n"
            f"Regime Shift: Log returns mean shifted from {mu_before:.5f} to {mu_after:.5f}"
        )
        print(statement)
        print("\n")

if __name__ == "__main__":
    run_analysis()
