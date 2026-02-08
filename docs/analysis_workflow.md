# Data Analysis Workflow
**Project**: Brent Oil Price Change Point Analysis  
**Client**: Birhan Energies  
**Date**: February 2026

## 1. Overview

This document outlines the systematic approach for analyzing how major political and economic events affect Brent oil prices using Bayesian change point detection methods. The analysis aims to provide actionable intelligence for investors, policymakers, and energy companies navigating the complexities of the global energy market.

## 2. Analysis Workflow Steps

### Step 1: Data Collection and Understanding
**Activities**:
- Load historical Brent oil price data (May 1987 - September 2022)
- Research and compile geopolitical events dataset (10-15 major events)
- Review domain literature on change point analysis and Bayesian inference

**Outputs**:
- Raw price data in CSV format
- Geopolitical events dataset with dates, descriptions, and categories
- Understanding of data characteristics and limitations

### Step 2: Exploratory Data Analysis (EDA)
**Activities**:
- Convert date formats and handle missing values
- Visualize historical price trends over time
- Analyze time series properties:
  - **Trend analysis**: Identify long-term patterns and shifts
  - **Stationarity testing**: Apply Augmented Dickey-Fuller (ADF) and KPSS tests
  - **Volatility patterns**: Calculate rolling standard deviation, examine volatility clustering
- Calculate and analyze log returns: `log(price_t) - log(price_{t-1})`

**Outputs**:
- Data quality report
- Visualization suite (time series plots, distribution plots, ACF/PACF)
- Statistical test results for stationarity
- Insights on data characteristics informing modeling choices

### Step 3: Bayesian Change Point Modeling
**Activities**:
- Define the Bayesian change point model using PyMC:
  - Specify prior distributions for switch point (tau)
  - Define parameters for "before" and "after" regimes (μ₁, μ₂, σ)
  - Implement switch function for regime selection
  - Define likelihood function
- Run MCMC sampling to estimate posterior distributions
- Check for convergence using R-hat statistics and trace plots

**Outputs**:
- Fitted PyMC model
- Posterior distributions for all parameters
- Convergence diagnostics
- Saved model artifacts

### Step 4: Model Interpretation and Change Point Identification
**Activities**:
- Extract and visualize posterior distribution of tau (change point)
- Identify most probable change point dates with credible intervals
- Quantify magnitude of shifts in price behavior parameters
- Assess uncertainty in change point detection

**Outputs**:
- List of detected change points with probabilities
- Visualizations of posterior distributions
- Quantitative impact statements (e.g., "X% shift in mean price")

### Step 5: Event Association and Causal Hypothesis
**Activities**:
- Compare detected change point dates with geopolitical event timeline
- Identify temporal proximity between events and change points
- Formulate evidence-based hypotheses about event-price relationships
- **Critical**: Distinguish between statistical correlation and causal relationships

**Outputs**:
- Event-change point association matrix
- Timeline visualization showing events and detected changes
- Documented hypotheses with supporting evidence
- Discussion of correlation vs. causation limitations

### Step 6: Insight Generation and Communication
**Activities**:
- Synthesize findings into actionable insights
- Create stakeholder-specific summaries:
  - **Investors**: Risk signals and market timing insights
  - **Policymakers**: Impact of policy decisions on market stability
  - **Energy companies**: Planning implications for operational decisions
- Develop interactive dashboard for exploration

**Outputs**:
- Executive summary report
- Detailed technical report with methodology
- Interactive dashboard (Flask backend + React frontend)
- Presentation materials

## 3. Tools and Technologies

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Data Analysis | Python, Pandas, NumPy | Data manipulation and preparation |
| Statistical Modeling | PyMC, ArviZ | Bayesian change point detection |
| Visualization | Matplotlib, Seaborn | Static visualizations |
| Backend API | Flask, Flask-CORS | Serve analysis results |
| Frontend Dashboard | React, Recharts | Interactive visualizations |
| Development | Jupyter Notebooks | Exploratory analysis and documentation |

## 4. Quality Assurance

- **Reproducibility**: All analysis code in version-controlled Jupyter notebooks
- **Validation**: Convergence diagnostics (R-hat ≈ 1.0) for Bayesian models
- **Documentation**: Inline code comments and markdown explanations
- **Peer Review**: Code review before merging to main branch

## 5. Communication Channels

### Internal Team
- **GitHub**: Code repository, issue tracking, pull requests
- **Slack**: #all-week11 channel for quick questions and updates
- **Jupyter Notebooks**: Document analysis process with narrative explanations

### Stakeholders
- **Executive Report**: 2-3 page PDF summary with key findings
- **Technical Report**: Comprehensive blog-post format (Medium-style) with methodology
- **Interactive Dashboard**: Web-based tool for exploring event-price relationships
- **Presentation**: Slide deck for stakeholder meetings

### Deliverable Formats
- **Written Reports**: PDF and Markdown formats
- **Code**: Python scripts and Jupyter notebooks on GitHub
- **Visualizations**: High-resolution PNG images and interactive HTML
- **Dashboard**: Deployed web application with API documentation

## 6. Timeline and Milestones

| Milestone | Due Date | Status |
|-----------|----------|--------|
| Task 1: Foundation | Feb 08, 2026 (Interim) | In Progress |
| Task 2: Modeling | Feb 10, 2026 (Final) | Pending |
| Task 3: Dashboard | Feb 10, 2026 (Final) | Pending |

## 7. Success Criteria

- **Statistical rigor**: Properly specified Bayesian models with convergence
- **Interpretability**: Clear explanations of technical concepts for non-technical stakeholders
- **Actionability**: Insights that inform specific decisions
- **Transparency**: Well-documented assumptions and limitations
- **Usability**: Interactive dashboard that enables self-service exploration
