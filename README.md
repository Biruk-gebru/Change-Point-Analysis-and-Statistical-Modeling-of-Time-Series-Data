# Brent Oil Price Change Point Analysis

## Overview
This project analyzes how major political and economic events affect Brent oil prices using Bayesian change point detection methods. The analysis focuses on identifying key events that have significantly impacted Brent oil prices over the past decade and quantifying their effects using statistical modeling.

## Business Context
**Client**: Birhan Energies - Leading consultancy firm specializing in data-driven insights for the energy sector

**Objective**: Provide actionable intelligence to help investors, policymakers, and energy companies navigate the complexities of the global energy market.

## Project Structure
```
.
├── notebooks/          # Jupyter notebooks for analysis
├── data/
│   ├── raw/           # Raw Brent oil price data
│   ├── processed/     # Processed and cleaned data
│   └── events/        # Compiled geopolitical events dataset
├── models/            # Saved PyMC models and results
├── backend/           # Flask API
│   ├── app/          # Flask application code
│   └── tests/        # Backend tests
├── frontend/          # React dashboard
├── docs/              # Analysis documentation
├── reports/           # Generated reports (interim & final)
├── scripts/           # Utility scripts
└── README.md
```

## Tasks

### Task 1: Laying the Foundation for Analysis
- Define data analysis workflow
- Research and compile event data (10-15 key events)
- Document assumptions and limitations
- Analyze time series properties (trend, stationarity, volatility)
- Explain change point models and expected outputs

**Deliverables**:
- 1-2 page document outlining analysis steps
- Structured CSV with dates and event descriptions
- Documentation of assumptions and limitations

### Task 2: Change Point Modeling and Insight Generation
- Data preparation and exploratory data analysis
- Build Bayesian change point model using PyMC
- Interpret model outputs and identify change points
- Associate detected changes with geopolitical events
- Quantify impacts of major events on price shifts

**Deliverables**:
- Jupyter notebook with complete analysis code
- Visualizations of posterior distributions and change points
- Written interpretation of results with quantified impacts

### Task 3: Developing Interactive Dashboard
- Flask backend with REST APIs for data serving
- React frontend with interactive visualizations
- Event correlation and drill-down capabilities
- Responsive design for multiple devices

**Deliverables**:
- Working Flask backend with documented API endpoints
- React frontend with interactive visualizations
- Screenshots demonstrating dashboard functionality
- Setup instructions

## Technology Stack
- **Analysis**: Python, PyMC, Pandas, NumPy, Matplotlib
- **Backend**: Flask, Flask-CORS
- **Frontend**: React, Recharts/D3.js
- **Statistical Methods**: Bayesian inference, MCMC sampling

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Installation
(Instructions to be added)

## Key Dates
- **Interim Submission**: Sunday, 08 Feb 2026, 8:00 PM UTC (Task 1)
- **Final Submission**: Tuesday, 10 Feb 2026, 8:00 PM UTC (Tasks 1-3)

## References
See [docs/references.md](docs/references.md) for a complete list of references.

## License
This project is part of the 10 Academy KAIM Week 11 Challenge.
