#!/usr/bin/env python3
"""
Bayesian Change Point Detection for Brent Oil Prices
Task 2: Change Point Modeling and Insight Generation

This script builds a Bayesian change point model using PyMC to detect
structural breaks in Brent oil prices.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pymc as pm
import arviz as az
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set plotting style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("=" * 70)
print("BAYESIAN CHANGE POINT DETECTION: Brent Oil Prices")
print("=" * 70)

# ============================================================================
# 1. DATA PREPARATION
# ============================================================================
print("\n[1/6] Loading and preparing data...")

# Load data
df = pd.read_csv('../data/raw/BrentOilPrices.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)
df = df.sort_values('Date').reset_index(drop=True)

# Focus on recent decade (2012-2022) to align with events
df_recent = df[df['Date'] >= '2012-01-01'].copy()

# Calculate log returns
df_recent['Log_Return'] = np.log(df_recent['Price'] / df_recent['Price'].shift(1))
df_recent = df_recent.dropna()

# Prepare data for modeling
log_returns = df_recent['Log_Return'].values
dates = df_recent['Date'].values
n_observations = len(log_returns)

print(f"✓ Data loaded: {n_observations} observations ({dates[0]} to {dates[-1]})")
print(f"✓ Log returns range: [{log_returns.min():.4f}, {log_returns.max():.4f}]")

# ============================================================================
# 2. BUILD BAYESIAN CHANGE POINT MODEL (Single Change Point)
# ============================================================================
print("\n[2/6] Building Bayesian change point model...")

with pm.Model() as model:
    # Priors for the change point location
    # Discrete uniform over all possible time indices
    tau = pm.DiscreteUniform('tau', lower=0, upper=n_observations - 1)
    
    # Priors for mean returns before and after change point
    # Using weakly informative priors centered at 0
    mu_before = pm.Normal('mu_before', mu=0, sigma=0.1)
    mu_after = pm.Normal('mu_after', mu=0, sigma=0.1)
    
    # Priors for standard deviations before and after
    # Using half-normal as volatility must be positive
    sigma_before = pm.HalfNormal('sigma_before', sigma=0.05)
    sigma_after = pm.HalfNormal('sigma_after', sigma=0.05)
    
    # Switch function: determines which parameters to use
    # For each time index, use "before" params if t < tau, else "after" params
    idx = np.arange(n_observations)
    mu = pm.math.switch(tau >= idx, mu_before, mu_after)
    sigma = pm.math.switch(tau >= idx, sigma_before, sigma_after)
    
    # Likelihood: observed log returns
    returns = pm.Normal('returns', mu=mu, sigma=sigma, observed=log_returns)
    
print("✓ Model structure:")
print(f"  - Change point (tau): DiscreteUniform(0, {n_observations-1})")
print(f"  - Mean before (mu_before): Normal(0, 0.1)")
print(f"  - Mean after (mu_after): Normal(0, 0.1)")
print(f"  - Std before (sigma_before): HalfNormal(0.05)")
print(f"  - Std after (sigma_after): HalfNormal(0.05)")

# ============================================================================
# 3. RUN MCMC SAMPLING
# ============================================================================
print("\n[3/6] Running MCMC sampling...")
print("This may take a few minutes...")

with model:
    # Sample from the posterior
    trace = pm.sample(
        draws=2000,
        tune=1000,
        chains=2,
        cores=2,
        target_accept=0.95,
        return_inferencedata=True,
        random_seed=42
    )

print("✓ Sampling complete!")

# ============================================================================
# 4. CONVERGENCE DIAGNOSTICS
# ============================================================================
print("\n[4/6] Checking convergence...")

# Summary statistics
summary = az.summary(trace, var_names=['tau', 'mu_before', 'mu_after', 'sigma_before', 'sigma_after'])
print("\nPosterior Summary:")
print(summary)

# Check R-hat (should be close to 1.0)
r_hats = summary['r_hat'].values
if np.all(r_hats < 1.1):
    print("\n✓ Convergence achieved: All R-hat values < 1.1")
else:
    print("\n⚠ Warning: Some R-hat values > 1.1, may need more samples")

# Save convergence diagnostics
summary.to_csv('../results/statistics/stat_bayesian_convergence.csv')
print("✓ Convergence diagnostics saved")

# ============================================================================
# 5. IDENTIFY CHANGE POINT
# ============================================================================
print("\n[5/6] Identifying change point...")

# Extract posterior samples for tau
tau_samples = trace.posterior['tau'].values.flatten()

# Most probable change point (mode of posterior)
tau_mode = int(np.bincount(tau_samples).argmax())
change_date = dates[tau_mode]

# Calculate credible interval
tau_lower = int(np.percentile(tau_samples, 2.5))
tau_upper = int(np.percentile(tau_samples, 97.5))
date_lower = dates[tau_lower]
date_upper = dates[tau_upper]

print(f"\n✓ DETECTED CHANGE POINT:")
print(f"  - Most probable date: {pd.to_datetime(change_date).date()}")
print(f"  - 95% credible interval: [{pd.to_datetime(date_lower).date()}, {pd.to_datetime(date_upper).date()}]")
print(f"  - Index: {tau_mode} (95% CI: [{tau_lower}, {tau_upper}])")

# ============================================================================
# 6. QUANTIFY IMPACT
# ============================================================================
print("\n[6/6] Quantifying impact...")

# Extract parameter posterior samples
mu_before_samples = trace.posterior['mu_before'].values.flatten()
mu_after_samples = trace.posterior['mu_after'].values.flatten()
sigma_before_samples = trace.posterior['sigma_before'].values.flatten()
sigma_after_samples = trace.posterior['sigma_after'].values.flatten()

# Calculate mean change
mean_change = mu_after_samples.mean() - mu_before_samples.mean()
mean_change_pct = mean_change * 100

# Probability that mean increased
prob_increase = (mu_after_samples > mu_before_samples).mean()

# Volatility change
vol_change = sigma_after_samples.mean() - sigma_before_samples.mean()
vol_change_pct = (vol_change / sigma_before_samples.mean()) * 100

print(f"\n✓ IMPACT QUANTIFICATION:")
print(f"  - Mean daily return shift: {mean_change:.6f} ({mean_change_pct:+.4f}%)")
print(f"  - Probability mean increased: {prob_increase:.2%}")
print(f"  - Volatility change: {vol_change:+.6f} ({vol_change_pct:+.2f}%)")

# Save impact summary
impact_df = pd.DataFrame({
    'Metric': ['Change Point Date', 'Date Lower CI', 'Date Upper CI',
               'Mean Before', 'Mean After', 'Mean Change', 'Prob(Increase)',
               'Volatility Before', 'Volatility After', 'Volatility Change %'],
    'Value': [
        str(pd.to_datetime(change_date).date()),
        str(pd.to_datetime(date_lower).date()),
        str(pd.to_datetime(date_upper).date()),
        f"{mu_before_samples.mean():.6f}",
        f"{mu_after_samples.mean():.6f}",
        f"{mean_change:.6f}",
        f"{prob_increase:.4f}",
        f"{sigma_before_samples.mean():.6f}",
        f"{sigma_after_samples.mean():.6f}",
        f"{vol_change_pct:.2f}%"
    ]
})
impact_df.to_csv('../results/statistics/stat_change_point_impact.csv', index=False)
print("✓ Impact summary saved")

# ============================================================================
# 7. VISUALIZATIONS
# ============================================================================
print("\nGenerating visualizations...")

# Figure 1: Posterior distribution of tau
fig, ax = plt.subplots(figsize=(14, 5))
ax.hist(tau_samples, bins=50, density=True, alpha=0.7, edgecolor='black')
ax.axvline(tau_mode, color='red', linestyle='--', linewidth=2, label=f'Mode: {pd.to_datetime(change_date).date()}')
ax.axvline(tau_lower, color='blue', linestyle=':', linewidth=1.5, label='95% CI')
ax.axvline(tau_upper, color='blue', linestyle=':', linewidth=1.5)
ax.set_xlabel('Time Index')
ax.set_ylabel('Posterior Density')
ax.set_title('Posterior Distribution of Change Point (τ)', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../results/figures/fig_tau_posterior.png', dpi=300, bbox_inches='tight')
print("✓ Saved: fig_tau_posterior.png")

# Figure 2: Parameter posterior distributions
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

ax = axes[0, 0]
ax.hist(mu_before_samples, bins=50, alpha=0.7, label='Before', color='blue')
ax.hist(mu_after_samples, bins=50, alpha=0.7, label='After', color='orange')
ax.set_xlabel('Daily Log Return')
ax.set_ylabel('Density')
ax.set_title('Mean Return Before vs After', fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

ax = axes[0, 1]
ax.hist(sigma_before_samples, bins=50, alpha=0.7, label='Before', color='blue')
ax.hist(sigma_after_samples, bins=50, alpha=0.7, label='After', color='orange')
ax.set_xlabel('Standard Deviation')
ax.set_ylabel('Density')
ax.set_title('Volatility Before vs After', fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

ax = axes[1, 0]
change_samples = mu_after_samples - mu_before_samples
ax.hist(change_samples, bins=50, alpha=0.7, color='green', edgecolor='black')
ax.axvline(0, color='red', linestyle='--', linewidth=2)
ax.set_xlabel('Change in Mean Return')
ax.set_ylabel('Density')
ax.set_title(f'Distribution of Mean Change (P(increase) = {prob_increase:.2%})', fontweight='bold')
ax.grid(True, alpha=0.3)

ax = axes[1, 1]
vol_change_samples = (sigma_after_samples - sigma_before_samples) / sigma_before_samples * 100
ax.hist(vol_change_samples, bins=50, alpha=0.7, color='purple', edgecolor='black')
ax.axvline(0, color='red', linestyle='--', linewidth=2)
ax.set_xlabel('Volatility Change (%)')
ax.set_ylabel('Density')
ax.set_title('Distribution of Volatility Change', fontweight='bold')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../results/figures/fig_parameter_posteriors.png', dpi=300, bbox_inches='tight')
print("✓ Saved: fig_parameter_posteriors.png")

# Figure 3: Price series with change point
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(dates, df_recent['Price'].values, linewidth=1, color='darkblue', alpha=0.7)
ax.axvline(change_date, color='red', linestyle='--', linewidth=2, label=f'Change Point: {pd.to_datetime(change_date).date()}')
ax.axvspan(date_lower, date_upper, alpha=0.2, color='red', label='95% CI')
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Price (USD/barrel)', fontsize=12)
ax.set_title('Brent Oil Prices with Detected Change Point', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../results/figures/fig_changepoint_on_prices.png', dpi=300, bbox_inches='tight')
print("✓ Saved: fig_changepoint_on_prices.png")

# Figure 4: Trace plots
az.plot_trace(trace, var_names=['tau', 'mu_before', 'mu_after', 'sigma_before', 'sigma_after'], figsize=(14, 10))
plt.tight_layout()
plt.savefig('../results/figures/fig_trace_plots.png', dpi=300, bbox_inches='tight')
print("✓ Saved: fig_trace_plots.png")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("BAYESIAN CHANGE POINT DETECTION COMPLETE")
print("=" * 70)
print(f"\nChange Point: {pd.to_datetime(change_date).date()}")
print(f"Mean Return Shift: {mean_change_pct:+.4f}%")
print(f"Volatility Change: {vol_change_pct:+.2f}%")
print("\nResults saved to ../results/")
print("  - Statistics: stat_bayesian_convergence.csv, stat_change_point_impact.csv")
print("  - Figures: 4 PNG files")
print("=" * 70)
