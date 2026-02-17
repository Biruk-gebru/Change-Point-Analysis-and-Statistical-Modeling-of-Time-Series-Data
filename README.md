# Brent Oil Price Change Point Analysis

[![CI Pipeline](https://github.com/Biruk-gebru/Change-Point-Analysis-and-Statistical-Modeling-of-Time-Series-Data/actions/workflows/test.yml/badge.svg)](https://github.com/Biruk-gebru/Change-Point-Analysis-and-Statistical-Modeling-of-Time-Series-Data/actions/workflows/test.yml)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-312/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
This project analyzes how major political and economic events affect Brent oil prices using Bayesian change point detection methods. The analysis focuses on identifying key events that have significantly impacted Brent oil prices over the past decade and quantifying their effects using statistical modeling.

## Key Results
- **Volatility Increase**: Identified ~127% increase in market volatility following the 2019 Iran sanctions waiver expiration
- **Predictive Power**: Model detected regime shift approximately 20 days before official policy announcement
- **Production Readiness**: Achieved 100% type hint coverage, 7/7 passing tests, and automated CI/CD pipeline

## Business Context
**Client**: Birhan Energies - Leading consultancy firm specializing in data-driven insights for the energy sector

**Objective**: Provide actionable intelligence to help investors, policymakers, and energy companies navigate the complexities of the global energy market.

## Quick Start

### Using Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/Biruk-gebru/Change-Point-Analysis-and-Statistical-Modeling-of-Time-Series-Data.git
cd Change-Point-Analysis-and-Statistical-Modeling-of-Time-Series-Data

# Start all services
docker-compose up -d

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:5000/api
```

### Manual Setup
See [Installation & Setup](#installation--setup) section below.

## Project Structure
```
.
├── backend/            # Flask REST API (Python)
│   ├── app/           # Application logic with type hints
│   │   ├── services.py   # Data service layer
│   │   └── routes.py     # API endpoints
│   ├── tests/         # Pytest test suite (7 tests)
│   ├── Dockerfile     # Backend containerization
│   └── run.py         # Entry point
├── frontend/          # React dashboard (JavaScript)
│   ├── src/           # React components
│   ├── Dockerfile     # Multi-stage build with Nginx
│   └── nginx.conf     # Production web server config
├── data/              # Data storage
│   ├── raw/           # Raw Brent oil price data
│   ├── processed/     # Processed and cleaned data
│   └── events/        # Compiled geopolitical events dataset
├── notebooks/         # Jupyter notebooks for analysis
├── models/            # Saved PyMC models and results
├── docs/              # Technical documentation
│   └── planning/      # Week 12 capstone planning artifacts
├── .github/workflows/ # CI/CD pipelines
│   ├── ci.yml         # Legacy linting workflow
│   └── test.yml       # Automated testing (NEW)
├── docker-compose.yml # Full-stack orchestration
└── DOCKER.md          # Docker deployment guide
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
- [x] **Interactive Price Charts**: Dynamic Recharts implementation with date-range filters (1Y, 5Y, All).
- [x] **Regime Shift Overlays**: Change point markers automatically overlaid on historical price data.
- [x] **Event Correlation**: Visual links between price shocks and documented geopolitical events.
- [x] **Responsive UI**: Optimized for all screen sizes using Tailwind CSS grid and flexbox.

#### Dashboard Features & Views:
1. **Analytics View (Main)**:
   - **Trend Chart**: Visualizes the last 10+ years of Brent oil prices.
   - **Date Range Controls**: Toggle between 1-year, 5-year, and full dataset views.
   - **Change Point Markers**: Red dashed line indicating the model's most probable regime shift date.
2. **Event Timeline (Sidebar)**:
   - **Categorized Events**: Scrollable list of 15 major events (Conflict, Sanctions, OPEC).
   - **Date Sync**: Each event displays the precise date, category, and historical context.
3. **KPI Cards**:
   - **Volatility Shift**: Quantified % change in market volatility after the detected change point.
   - **Mean Change**: Shift in average price returns observed after the event.

#### Responsiveness Behavior:
- **Desktop**: 12-column grid with a 3:1 ratio between the chart and the event sidebar.
- **Tablet/Mobile**: Single-column vertical layout where the sidebar drops below the chart for optimal readability on touch devices.
- **Dynamic Sizing**: Charts utilize `ResponsiveContainer` to adapt height and width fluidly.

### Setup & Execution

#### 1. Backend API (Flask)
```bash
cd backend
pip install -r ../requirements.txt
python3 run.py
```
*API serves on localhost:5000*

#### 2. Frontend Dashboard (React)
```bash
cd frontend
npm install
npm start
```
*Dashboard serves on localhost:3000*


## Technology Stack
- **Analysis**: Python, PyMC, Pandas, NumPy, Matplotlib
- **Backend**: Flask, Flask-CORS
- **Frontend**: React, Recharts/D3.js
- **Statistical Methods**: Bayesian inference, MCMC sampling

## Installation & Setup

### Backend (Flask API)
1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```
2. **Install dependencies**:
   ```bash
   pip install -r ../requirements.txt
   ```
3. **Run the server**:
   ```bash
   python3 run.py
   ```
   The API will be available at `http://127.0.0.1:5000/api`.

### Frontend (React Dashboard)
1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```
2. **Install dependencies**:
   ```bash
   npm install
   ```
3. **Run the dashboard**:
   ```bash
   npm start
   ```
   The dashboard will open at `http://localhost:3000`.

## API Documentation

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/prices` | GET | Returns historical Brent oil prices (Date, Price) |
| `/api/events` | GET | Returns curated geopolitical events with categories and descriptions |
| `/api/changepoint` | GET | Returns summary of the detected regime shift and its quantified impact |
| `/api/changepoint/trace` | GET | Returns MCMC sampling results for model parameters |
| `/api/volatility` | GET | Returns daily stochastic volatility estimates |

## Analysis Insights

Our Bayesian analysis identified a significant structural change point in early 2019, closely associated with the **US ending Iran Sanctions Waivers**. Post-event analysis revealed:
- **Volatility Increase**: Approximately **127%** increase in market volatility following the shift.
- **Regime Transition**: The market moved from a period of relative stability to one characterized by frequent high-magnitude shocks.
- **Model Efficacy**: The Bayesian model successfully "priced in" the shock approximately 20 days before the official waiver expiration.

## Dashboard Preview
![Birhan Energies Dashboard](results/figures/birhanDash.png)

## Week 12 Capstone Improvements

This project was significantly enhanced for the Week 12 Capstone submission with the following production-grade improvements:

### Engineering Excellence
- **Type Safety**: Added comprehensive type hints to all backend functions (100% coverage)
- **Structured Logging**: Implemented production-ready logging with proper error tracking
- **Code Quality**: Refactored services and routes for maintainability and clarity

### Reliability & Testing
- **Test Suite**: Created 7 comprehensive tests (3 API smoke tests + 4 service unit tests)
- **Test Coverage**: 100% pass rate with proper fixtures and mocking
- **CI/CD Pipeline**: Automated testing via GitHub Actions on every push

### Deployment Readiness
- **Dockerization**: Multi-stage builds for both backend (Flask + Python) and frontend (React + Nginx)
- **Orchestration**: Docker Compose for single-command full-stack deployment
- **Production Configuration**: Nginx reverse proxy with gzip compression and static asset caching

See [docs/planning/](docs/planning/) for detailed planning artifacts including Gap Analysis, Implementation Plan, and progress reports.

## Future Improvements

With additional time and resources, the following enhancements would further strengthen this project:

1. **Advanced ML Features**
   - Implement SHAP-based explanations for non-technical stakeholders
   - Add multi-variate change point detection (incorporating volume, news sentiment)
   - Deploy ensemble models for improved forecast accuracy

2. **Production Infrastructure**
   - Add Redis caching layer for API responses
   - Implement rate limiting and authentication
   - Set up monitoring with Prometheus/Grafana
   - Create automated deployment pipeline (Kubernetes)

3. **User Experience**
   - Real-time data streaming from financial APIs
   - Custom alert system for significant regime shifts
   - Mobile-responsive dashboard enhancements
   - Export functionality for reports (PDF/Excel)

4. **Data Expansion**
   - Incorporate additional crude oil benchmarks (WTI, Dubai)
   - Add macroeconomic indicators (inflation, interest rates)
   - Integrate social media sentiment analysis

## Author

**Biruk Gebru Jember**  
Artificial Intelligence Mastery Program - 10 Academy  
Week 12 Capstone Project

📧 [birukjember2004@gmail.com](mailto:birukjember2004@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/biruk-gebru-jember)  
💻 [GitHub](https://github.com/Biruk-gebru)

---

## License

This project is part of the 10 Academy KAIM Week 11 Challenge.
