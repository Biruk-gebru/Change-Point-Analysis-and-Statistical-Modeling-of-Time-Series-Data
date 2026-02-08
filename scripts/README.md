# Task 2: Bayesian Change Point Modeling

## Overview
This directory contains the implementation of Bayesian change point detection for Brent oil prices using PyMC.

## Scripts

### `bayesian_changepoint.py`
Main script for detecting structural breaks in oil prices.

**Features**:
- Single change point Bayesian model
- MCMC sampling with convergence diagnostics
- Posterior distributions for all parameters
- Impact quantification with credible intervals
- 4 visualizations saved to `results/figures/`

**Run**:
```bash
cd scripts
python bayesian_changepoint.py
```

**Outputs**:
- `../results/statistics/stat_bayesian_convergence.csv` - R-hat and ESS values
- `../results/statistics/stat_change_point_impact.csv` - Impact summary
- `../results/figures/fig_tau_posterior.png` - Change point posterior
- `../results/figures/fig_parameter_posteriors.png` - Before/after parameters
- `../results/figures/fig_changepoint_on_prices.png` - Price series with change point
- `../results/figures/fig_trace_plots.png` - MCMC diagnostics

## Model Specification

### Priors:
- τ (change point): DiscreteUniform(0, n-1)
- μ_before, μ_after: Normal(0, 0.1)
- σ_before, σ_after: HalfNormal(0.05)

### Likelihood:
- returns ~ Normal(μ, σ) where μ and σ switch at τ

### Sampling:
- 2000 draws, 1000 tuning
- 2 chains, target_accept=0.95

## Next Steps

1. Run `bayesian_changepoint.py` to detect change point
2. Check convergence diagnostics (R-hat < 1.1)
3. Review change point date and compare with events
4. Analyze impact quantification results
5. Use outputs for final report
