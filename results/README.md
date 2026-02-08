# Results Organization

This directory contains all analysis results for easy reference in reports.

## Structure

```
results/
├── figures/        # All plots and visualizations saved as PNG/PDF
├── statistics/     # Statistical summaries, test results, metrics (CSV/JSON)
└── models/         # Model outputs, posterior distributions, convergence diagnostics
```

## Naming Convention

Use descriptive names with prefixes:
- `fig_*.png` - Figures/plots
- `stat_*.csv` - Statistical summaries
- `model_*.pkl` - Saved models

## Usage in Notebooks

Save figures:
```python
plt.savefig('../results/figures/fig_price_timeseries.png', dpi=300, bbox_inches='tight')
```

Save statistics:
```python
summary_df.to_csv('../results/statistics/stat_descriptive.csv', index=False)
```

This makes it easy to reference results in reports without re-running notebooks.
