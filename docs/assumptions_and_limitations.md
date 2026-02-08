# Assumptions and Limitations

## 1. Key Assumptions

### 1.1 Data Assumptions
- **Completeness**: The historical Brent oil price data (1987-2022) is complete and accurate
- **Representativeness**: Daily closing prices adequately capture market dynamics
- **Data Quality**: Price data has been properly adjusted for any splits or anomalies

### 1.2 Event Selection Assumptions
- **Materiality**: The 14 compiled geopolitical events represent the most significant market-moving events in the 2011-2022 period
- **Event Dates**: The documented event dates accurately reflect when markets began to price in the information
- **Event Independence**: Events are treated as independent, though in reality they may have compounding or interactive effects

### 1.3 Modeling Assumptions
- **Structural Breaks**: Price behavior can be characterized by discrete regime changes (change points)
- **Finite Change Points**: There are a limited number of major structural breaks in the time series
- **Stationarity Within Regimes**: Between change points, the statistical properties of returns remain relatively stable
- **Parameter Stability**: Mean and variance parameters are constant within each regime
- **Bayesian Priors**: Chosen prior distributions (uniform for tau, normal for means) adequately represent prior uncertainty

### 1.4 Market Assumptions
- **Efficiency**: Markets incorporate new information relatively quickly (though not instantaneously)
- **Liquidity**: Brent oil market is sufficiently liquid that observed prices reflect true market value
- **Global Benchmark**: Brent crude serves as a reliable global oil price benchmark

## 2. Critical Limitation: Correlation vs. Causation

### 2.1 The Distinction
**This is the most important limitation of this analysis.**

- **Correlation in Time**: The analysis can identify when a statistical change point occurs in close temporal proximity to a geopolitical event
- **Causal Impact**: The analysis **cannot conclusively prove** that the event **caused** the price change

### 2.2 Why Causation Cannot Be Proven

#### Confounding Variables
- Multiple events or factors may occur simultaneously
- Example: OPEC decisions may coincide with changing demand patterns
- Cannot isolate the effect of a single event without controlled experiments (impossible in global markets)

#### Reverse Causality
- Oil price changes might influence political decisions, not just vice versa
- Example: Low prices may trigger OPEC production cuts

#### Anticipation Effects
- Markets may react before events officially occur based on expectations
- The statistical change point may precede the formal event announcement

#### Lagged Effects
- Some events have delayed impacts as markets gradually digest information
- A change point days or weeks after an event may or may not be related

### 2.3 What We Can Claim
✅ **Valid Claims**:
- "A change point was detected on [date] with X% posterior probability"
- "This change point is temporally proximate to [event]"
- "The change represents a Y% shift in average price behavior"
- "The association suggests [event] as a plausible contributing factor"

❌ **Invalid Claims**:
- "Event X caused the price change"
- "Event X increased prices by Y%"
- "Event X was the primary driver of the change"

### 2.4 Strengthening Causal Inference
To move from correlation toward causal inference would require:
- **Counterfactual Analysis**: Compare actual outcomes to what would have happened without the event (impossible to observe)
- **Multiple Data Sources**: Incorporate supply/demand fundamentals, inventory levels, production data
- **Mechanism Analysis**: Demonstrate  the causal pathway (e.g., sanctions → reduced supply → higher prices)
- **Natural Experiments**: Leverage situations where events affect some markets but not others
- **Structural Models**: Build economic models that explicitly represent causal relationships

## 3. Technical Limitations

### 3.1 Model Limitations
- **Single Change Point Models**: Basic models detect one change point; reality likely has multiple overlapping regime changes
- **Discrete Breaks**: Assumes abrupt changes rather than gradual transitions
- **Linear Dynamics**: Does not capture non-linear relationships or threshold effects
- **Volatility**: Simple models may not adequately capture time-varying volatility (GARCH effects)
- **Parameter Uncertainty**: Bayesian credible intervals reflect statistical uncertainty, not all sources of uncertainty

### 3.2 Data Limitations
- **Time Granularity**: Daily data may miss intraday volatility from breaking news
- **Single Series**: Analysis focuses only on Brent prices, not broader energy complex
- **Historical Scope**: Data from 1987-2022 may not reflect current market structure
- **Missing Variables**: Numerous factors affect prices beyond documented events:
  - Global GDP growth
  - Currency exchange rates (USD strength)
  - Inventory levels
  - Weather patterns
  - Technology changes (e.g., US shale revolution)
  - Speculation and financial flows

### 3.3 Computational Limitations
- **MCMC Convergence**: Posterior estimates depend on adequate sampling; convergence must be verified
- **Prior Sensitivity**: Results may be sensitive to choice of prior distributions
- **Model Selection**: No single "correct" model specification

## 4. Practical Implications

### 4.1 For Investors
- Use insights as **one input** among many for decision-making
- Recognize that past patterns may not predict future responses to similar events
- Understand that timing of market reactions is uncertain

### 4.2 For Policymakers
- Correlation evidence is useful for understanding historical market reactions
- Cannot assume identical policy actions will produce identical market responses
- Consider broader economic context, not just historical price patterns

### 4.3 For Energy Companies
- Historical event impacts inform scenario planning
- Build ranges of outcomes rather than point forecasts
- Recognize that operational decisions require multi-factor analysis

## 5. Future Work to Address Limitations

### 5.1 Enhanced Modeling
- Extend to **multiple change point models**
- Implement **Markov-switching models** to allow smooth regime transitions
- Incorporate **time-varying volatility** (GARCH-type models)
- Build **vector autoregression (VAR) models** with multiple related variables

### 5.2 Richer Data
- Integrate supply and demand fundamentals
- Include inventory data, production figures, refinery utilization
- Add macroeconomic indicators (GDP growth, inflation, exchange rates)
- Incorporate market sentiment and positioning data

### 5.3 Causal Methods
- Explore **event study methodology** from finance
- Investigate **synthetic control methods** for policy events
- Apply **Granger causality tests** for directional relationships
- Consider **instrumental variable** approaches where applicable

## 6. Conclusion

This analysis provides valuable insights into the **statistical associations** between geopolitical events and Brent oil prices. The Bayesian change point detection method rigorously identifies structural breaks with quantified uncertainty. However, users must understand the fundamental limitation: **correlation in time does not prove causation**.

The value lies not in definitive causal statements, but in:
- Identifying which events coincided with measurable market regime changes
- Quantifying the magnitude of those changes
- Building intuition about market dynamics
- Informing scenario analysis and risk management

All insights should be interpreted within this framework of appropriate statistical caution.
