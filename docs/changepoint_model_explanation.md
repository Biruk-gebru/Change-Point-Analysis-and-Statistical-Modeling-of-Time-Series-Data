# Change Point Models: Purpose and Methodology

## 1. Introduction

Change point models are statistical methods designed to identify points in time where the underlying probability distribution of a time series undergoes a structural break. In the context of Brent oil price analysis, these models help us detect when market behavior fundamentally shifts—often in response to major geopolitical or economic events.

## 2. Purpose in Oil Price Analysis

### 2.1 Why Change Points Matter

**Traditional time series analysis** assumes statistical properties (mean, variance, autocorrelation) remain constant over time. However, oil markets exhibit clear regime changes:
- Peaceful periods → Geopolitical crisis → Different volatility
- Oversupply conditions → Production cuts → Different price levels
- Growing demand → Pandemic demand shock → Different dynamics

**Change point analysis** explicitly models these transitions, allowing us to:
1. **Identify** when structural breaks occur
2. **Quantify** the magnitude of shifts in price behavior
3. **Associate** breaks with potential causal events
4. **Segment** historical data into homogeneous periods for better modeling

### 2.2 Applications

- **Risk Management**: Understanding volatility regime changes helps traders manage position sizing
- **Policy Analysis**: Evaluating the market impact of regulatory or diplomatic actions
- **Strategic Planning**: Energy companies can align operational decisions with market regimes
- **Forecasting**: More accurate predictions by modeling distinct regimes separately

## 3. Types of Change Points

### 3.1 Mean Change Points
The average price level shifts while variance remains stable.

**Example**: OPEC production cut → Prices shift from $50/barrel average to $70/barrel average

### 3.2 Variance Change Points
Average price stays similar, but volatility changes.

**Example**: Geopolitical crisis → Prices remain ~$80/barrel but daily fluctuations increase from ±$2 to ±$8

### 3.3 Combined Change Points
Both mean and variance shift simultaneously.

**Example**: COVID-19 pandemic → Prices crash (mean shift) AND volatility spikes (variance shift)

## 4. Bayesian Change Point Model

### 4.1 Model Components

#### a) The Switch Point (τ)
- **Definition**: The time index where the regime change occurs
- **Prior Distribution**: Discrete Uniform over all possible time points
  - Reflects complete prior uncertainty about when the change occurred
- **Posterior Distribution**: Updated belief after seeing the data
  - A sharp peak indicates high certainty about the change point location

#### b) Regime Parameters
- **Before Parameters** (μ₁, σ₁): Characterize behavior before the change point
- **After Parameters** (μ₂, σ₂): Characterize behavior after the change point
- **Prior Distributions**: Typically normal or half-normal distributions
  - Express initial belief about plausible parameter values

#### c) Switch Function
The model uses τ to determine which parameters apply at each time point:
```
if t < τ:
    use μ₁, σ₁
else:
    use μ₂, σ₂
```

#### d) Likelihood Function
Connects the model to observed data:
- For each observed price (or log return), calculate probability under the selected regime parameters
- Product of all these probabilities gives the overall likelihood

### 4.2 Why Bayesian?

**Bayesian methods** offer several advantages:

1. **Quantified Uncertainty**: Provides full posterior distributions, not just point estimates
   - "τ is most likely day 1,245, with 95% credible interval [1,230, 1,260]"
   
2. **Probabilistic Statements**: Can make statements like "There's an 87% probability the change occurred within 2 weeks of the OPEC announcement"

3. **Incorporates Prior Knowledge**: Can encode expert judgment about plausible change point locations

4. **Handles Complexity**: Naturally extends to multiple change points, hierarchical structures

5. **No Asymptotics Needed**: Works well with finite samples

### 4.3 MCMC Sampling

Bayesian change point models use **Markov Chain Monte Carlo (MCMC)** to estimate posterior distributions:

1. **Initialize**: Start with random parameter values
2. **Propose**: Suggest a new value for one parameter
3. **Evaluate**: Calculate how well it fits the data
4. **Accept/Reject**: Probabilistically decide whether to keep the new value
5. **Iterate**: Repeat thousands of times until convergence

The result is a collection of samples from the posterior distribution, allowing us to:
- Estimate most probable values
- Calculate credible intervals
- Generate predictive distributions

## 5. Expected Outputs

### 5.1 Change Point Location

**Output**: Posterior distribution over τ

**Visualization**: Histogram or density plot showing probability for each time index

**Interpretation**:
- **Sharp peak**: High certainty about change point date
  - Example: "99% probability change occurred between March 5-12, 2020"
- **Broad distribution**: Uncertainty about exact timing
  - Example: "Change likely occurred sometime in Q2 2018"
- **Multiple peaks**: Evidence for multiple change points

### 5.2 Parameter Estimates

**Output**: Posterior distributions for μ₁, μ₂, σ₁, σ₂

**Visualization**: Density plots, credible intervals

**Interpretation**:
- Magnitude of shift: "Mean log return changed from -0.02% to +0.15% per day"
- Uncertainty: "95% credible interval for μ₂ is [0.08%, 0.22%]"
- Volatility change: "Standard deviation doubled from 2% to 4%"

### 5.3 Probabilistic Impact Statements

**Example Outputs**:
- "There is a 95% probability that the regime change increased average daily returns"
- "The probability that  mean price shifted by more than $10/barrel is 78%"
- "Posterior probability of a change point within 30 days of Event X is 92%"

### 5.4 Model Diagnostics

**Convergence Checks**:
- **R-hat statistic** (Gelman-Rubin): Should be ≈ 1.0
  - Values > 1.1 suggest lack of convergence
- **Effective sample size**: Should be large (typically > 1000)
- **Trace plots**: Should look like "fuzzy caterpillars" without trends or patterns

### 5.5 Visualizations

**Common plots**:
1. **Time series with change point**: Raw data with vertical line at estimated τ
2. **Posterior distribution of τ**: Probability across time of change point
3. **Regime-specific fits**: Before/after segments with fitted parameters
4. **Posterior predictive checks**: Model predictions vs. actual data

## 6. Limitations of Change Point Models

### 6.1 What They Can Do
✅ Detect structural breaks in time series  
✅ Quantify uncertainty about break timing  
✅ Estimate magnitude of parameter shifts  
✅ Segment historical data into regimes  

### 6.2What They Cannot Do
❌ **Prove causation**: Can only identify association in time  
❌ **Predict future changes**: Cannot forecast when next change will occur  
❌ **Detect gradual transitions**: Assumes abrupt breaks  
❌ **Capture all dynamics**: Simplified representation of complex reality  
❌ **Account for all factors**: Omitted variables may drive apparent changes  

### 6.3 Practical Challenges
- **Multiple change points**: Basic models detect only one break; reality often has many
- **Change point proximity**: Nearby breaks are difficult to separate
- **Parameter identifiability**: If no clear break exists, parameters may be poorly identified
- **Computational cost**: MCMC sampling can be slow for large datasets
- **Model specification**: Results can be sensitive to distributional assumptions

## 7. Extensions and Advanced Topics

### 7.1 Multiple Change Points
Extend the model to detect k change points:
- Requires specifying k or treating it as unknown (more complex)
- Can become computationally intensive

### 7.2 Time-Varying Parameters
Rather than discrete breaks, allow parameters to evolve smoothly:
- **Stochastic volatility models**: σ changes over time
- **Dynamic linear models**: μ evolves according to a random walk

### 7.3 Hierarchical Models
Model change points across multiple related time series:
- Example: Detect common change points across Brent, WTI, and Dubai crude
- Borrow strength across series for better estimates

### 7.4 Online Change Point Detection
Update change point estimates in real-time as new data arrives:
- Useful for algorithmic trading or real-time monitoring
- More complex than retrospective analysis

## 8. Conclusion

Change point models provide a rigorous statistical framework for identifying and quantifying structural breaks in Brent oil prices. By using Bayesian methods, we obtain not just point estimates, but full probability distributions that quantify our uncertainty.

The key value is in:
- **Objective detection** of regime changes
- **Quantified uncertainty** through posterior distributions
- **Principled framework** for associating events with price shifts

However, users must remember the limitations—especially that statistical association does not prove causation. Change point models answer "when did behavior change?" not "why did it change?" The latter requires domain expertise, economic theory, and careful interpretation of the statistical evidence.
