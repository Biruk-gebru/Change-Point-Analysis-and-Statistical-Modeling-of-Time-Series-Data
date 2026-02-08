import pandas as pd
import numpy as np
import pymc as pm
import arviz as az
import os

# Paths
DATA_PATH = '/home/karanos/kiam/week11/prod/data/raw/BrentOilPrices.csv'
OUTPUT_TRACE = '/home/karanos/kiam/week11/prod/data/processed/change_point_trace.nc'
OUTPUT_SUMMARY = '/home/karanos/kiam/week11/prod/data/processed/change_point_summary.csv'

def run_changepoint_model():
    print("Loading data...")
    if not os.path.exists(DATA_PATH):
        # Fallback to absolute path or adjust
        print(f"Error: Data file not found at {DATA_PATH}")
        return

    df = pd.read_csv(DATA_PATH)
        
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)
    df = df.sort_values('Date').reset_index(drop=True)
    df_recent = df[df['Date'] >= '2012-01-01'].copy()
    
    # Check for Log_Return column
    if 'Log_Return' not in df_recent.columns:
        df_recent['Log_Return'] = np.log(df_recent['Price'] / df_recent['Price'].shift(1))
    
    df_recent = df_recent.dropna()
    log_returns = df_recent['Log_Return'].values
    n_obs = len(log_returns)
    dates = df_recent['Date'].values
    
    print(f"Data loaded: {n_obs} observations.")

    print("Building model...")
    with pm.Model() as model:
        tau = pm.DiscreteUniform('tau', lower=0, upper=n_obs - 1)
        mu_before = pm.Normal('mu_before', mu=0, sigma=0.1)
        sigma_before = pm.HalfNormal('sigma_before', sigma=0.05)
        mu_after = pm.Normal('mu_after', mu=0, sigma=0.1)
        sigma_after = pm.HalfNormal('sigma_after', sigma=0.05)
        
        idx = np.arange(n_obs)
        mu = pm.math.switch(tau >= idx, mu_before, mu_after)
        sigma = pm.math.switch(tau >= idx, sigma_before, sigma_after)
        
        returns = pm.Normal('returns', mu=mu, sigma=sigma, observed=log_returns)
        
    print("Sampling...")
    with model:
        # Reduced samples for speed as per user preference in Task 3
        # Saving trace to netcdf
        trace = pm.sample(draws=1000, tune=1000, chains=2, return_inferencedata=True, random_seed=42)
        trace.to_netcdf(OUTPUT_TRACE)
    
    print(f"Trace saved to {OUTPUT_TRACE}")
    
    # Save summary
    summary = az.summary(trace, var_names=['tau', 'mu_before', 'mu_after', 'sigma_before', 'sigma_after'])
    summary.to_csv(OUTPUT_SUMMARY)
    
    # Calculate expected date of change
    tau_mean = summary.loc['tau', 'mean']
    tau_hdi_3 = summary.loc['tau', 'hdi_3%']
    tau_hdi_97 = summary.loc['tau', 'hdi_97%']
    
    idx_mean = int(tau_mean)
    idx_3 = int(tau_hdi_3)
    idx_97 = int(tau_hdi_97)

    if 0 <= idx_mean < len(dates):
        date_mean = dates[idx_mean]
        date_hdi_3 = dates[min(max(0, idx_3), len(dates)-1)]
        date_hdi_97 = dates[min(max(0, idx_97), len(dates)-1)]
        
        print(f"Change Point Detected at Index: {tau_mean:.2f} (HDI: {tau_hdi_3}-{tau_hdi_97})")
        print(f"Estimated Date: {date_mean}")
        print(f"Uncertainty Interval: {date_hdi_3} to {date_hdi_97}")
    else:
        print(f"Change Point index {idx_mean} out of bounds.")

if __name__ == "__main__":
    run_changepoint_model()
