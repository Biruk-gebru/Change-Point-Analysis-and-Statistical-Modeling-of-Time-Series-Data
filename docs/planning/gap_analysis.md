# Gap Analysis: Project Selection for Portfolio

## 🏆 Project Ranking
1. **[#1] Week 11: Brent Oil Price Change Point Analysis**
   - **Domain**: Fintech / Risk Analysis / Econometrics.
   - **Tech Stack**: React, Flask, PyMC (Bayesian Modeling).
   - **Why #1**: High complexity, strong "Wow" factor with full-stack implementation and advanced statistical modeling. Perfect alignment with "Risk" and "Forecasting" portfolio goals.

2. **[#2] Week 10: Ethiopia Financial Inclusion Forecasting**
   - **Domain**: Economic Forecasting / Policy Impact.
   - **Tech Stack**: Streamlit, Python.
   - **Why #2**: Strong data science project with clear forecasting goals. Code quality is actually *higher* initially, but the tech stack (Streamlit) is less "Production Engineering" impressive than a React/Flask app.

---

## 🔍 Gap Analysis vs. Production Standards

| Feature | Week 11 (Brent Oil) | Week 10 (Financial Inclusion) | Status |
| :--- | :--- | :--- | :--- |
| **Engineering Excellence** | 🔴 **Major Gap**<br>- No Type Hints found.<br>- No Logging implemented.<br>- Uses raw Dicts/DataFrames instead of Dataclasses. | 🟡 **Partial**<br>- Type hints present (`src/utils.py`).<br>- Logging implemented.<br>- Good modularity. | Week 11 needs significant refactoring. |
| **Reliability** | 🔴 **Critical Gap**<br>- `backend/tests` is **EMPTY**.<br>- Zero unit tests found. | 🟡 **Partial**<br>- One test file exists (`test_impact_model.py`).<br>- Uses `pytest`. | Week 11 needs a full test suite from scratch. |
| **CI/CD** | 🟡 **Partial**<br>- GitHub Action exists (`ci.yml`) but **only lints**.<br>- Does NOT run tests (because there are none). | 🟡 **Partial**<br>- GitHub Action exists but `test` job only runs `flake8`.<br>- Doesn't run the existing tests. | Both need pipeline upgrades to run actual tests. |
| **Explainability** | 🟢 **Good**<br>- Uses PyMC traces.<br>- Dashboard has "Change Point" overlays.<br>- Could be enhanced with SHAP/LIME. | 🟢 **Good**<br>- Event-Indicator Matrix.<br>- Clear "Impact" categorization. | Week 11 is strong but can be improved with better visual explainability. |
| **Deployment** | 🟢 **Good**<br>- React & Flask setup.<br>- Docker readiness is unconfirmed but structure supports it. | 🟢 **Good**<br>- Streamlit is deployment-ready.<br>- Requirements are clear. | Week 11 is closer to a "Real App" architecture. |

## 🚀 Recommendation
**I have selected Week 11 (Brent Oil)**. 
Refactoring this existing "Prototype" into a "Production-Grade System" will demonstrate exactly the skills I want to highlight:
1.  **Refactoring** legacy/research code into clean, typed, logged code.
2.  **Adding Testing** to an untestable codebase (high value signal).
3.  **Building CI/CD** for a full-stack application.
