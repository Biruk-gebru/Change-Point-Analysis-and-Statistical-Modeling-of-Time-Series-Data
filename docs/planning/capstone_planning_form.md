# Capstone Project Selection & Planning Form

## 📅 Interim vs. Final Submission Classification

| Submission | Focus | Deliverables |
| :--- | :--- | :--- |
| **Interim Submission**<br>(Mid-Week) | **Core Engineering Foundation** | 1. **Test Suite**: Functional `pytest` setup with >50% coverage.<br>2. **Refactoring**: Backend services typed and logged.<br>3. **CI/CD**: GitHub Actions pipeline running tests.<br>4. **Plan**: This planning document committed. |
| **Final Submission**<br>(End of Week) | **Polish & Production Readiness** | 1. **Full Coverage**: >80% Test Coverage.<br>2. **Deployment**: Docker files for Backend/Frontend.<br>3. **Explainability**: Enhanced "Change Point" insights in dashboard.<br>4. **Docs**: Complete `README.md` with architecture diagrams. |

---

## 📝 Form Responses

### **Which project have you selected for your capstone?**
**Week 11: Brent Oil Price Change Point Analysis**

### **Why did you choose this project?**
I chose this project because it offers the highest technical depth, combining a full-stack application (React + Flask) with advanced Bayesian statistical modeling (PyMC). It aligns perfectly with the Fintech portfolio goal of "Risk Analysis." Although the current codebase functions as a prototype, it lacks engineering rigor (tests, typing, CI/CD), making it the ideal candidate to demonstrate my ability to transform research code into a production-grade system.

### **What is the business problem your project solves?**
Investors and policymakers face significant financial risk because they cannot easily quantify how specific geopolitical events (like sanctions or conflicts) impact oil price volatility. This project solves this by using statistical change-point detection to mathematically identify regime shifts and quantify the "volatility shock" of events, enabling data-driven risk management.

### **What metrics define success for this project?**
1.  **Code Quality**: Achieve >90% Type Hint coverage in the backend to ensure type safety.
2.  **Reliability**: Increase Test Coverage from 0% to >80% using Pytest.
3.  **Automation**: Achieve a 100% success rate on a new CI/CD pipeline that runs both linting and automated tests on every push.

### **What was completed in the original project?**
1.  **Statistical Model**: A Bayesian Change Point detection model using PyMC.
2.  **Backend API**: A Flask application serving price data and event data.
3.  **Frontend Dashboard**: A React-based UI with interactive charts and event overlays.

### **What was NOT completed or needs improvement?**
1.  **Testing**: There are currently **zero** automated tests (no unit or integration tests), posing a high risk of regression.
2.  **Code Quality**: The codebase lacks Type Hints and structured logging, making it hard to maintain.
3.  **CI/CD**: The existing GitHub workflow only performs basic linting and does not execute any tests.
4.  **Deployment**: The application is not containerized (no Docker support).

### **What engineering improvements will you implement?**
1.  **Refactoring**: Rewrite the backend service layer using Python Type Hints and Dataclasses to enforce data structures.
2.  **Testing Strategy**: Implement a comprehensive `pytest` suite covering unit tests for logic and integration tests for API endpoints.
3.  **DevOps**: Build a robust CI/CD pipeline using GitHub Actions to automate testing and code quality checks.
4.  **Containerization**: Create Dockerfiles for both services to ensure reproducible deployments.

### **What is your biggest risk or blocker?**
**Risk**: Comprehensive refactoring of the backend (adding types and changing data structures) could break the contract with the Frontend, leading to a broken dashboard.
**Mitigation**: I will implement "Regression Testing" by writing integration tests for the current API endpoints *before* starting the refactoring. This ensures I have a safety net to verify functionality remains intact.

### **Day-by-Day Execution Plan**
*(Schedule starting Wednesday, Feb 11)*

*   **Wed Feb 11**: **Planning & Analysis**
    *   Conduct Gap Analysis of Week 11 and Week 10 projects.
    *   Select Week 11 and define the 5-Sprint Implementation Plan.
    *   Initial repo setup and cleanup.

*   **Thu Feb 12**: **Sprint 1 - Reliability Foundation**
    *   Install test dependencies (`pytest`, `httpx`).
    *   Write initial "Smoke Tests" for existing API endpoints to establish a baseline.
    *   Configure `conftest.py` for test fixtures.

*   **Fri Feb 13**: **Sprint 2 - Refactoring (Part 1)**
    *   Refactor `backend/app/services.py`: Add Type Hints and replace raw Dicts with Dataclasses.
    *   Implement structured Logging to replace `print` statements.

*   **Sat Feb 14**: **Sprint 2 - Refactoring (Part 2)**
    *   Update `backend/app/routes.py` to use the new typed services.
    *   Run Smoke Tests to ensure no regressions.
    *   Fix any broken tests resulting from strict typing.

*   **Sun Feb 15**: **Sprint 3 - CI/CD & Automation**
    *   Create `.github/workflows/test.yml`.
    *   Configure pipeline to run `pytest` and `flake8` on push.
    *   Address code style issues flagged by the linter.

*   **Mon Feb 16**: **Sprint 4 - Interim Submission Prep**
    *   Verify all tests pass in CI.
    *   Polish the README with "How to Run Tests" instructions.
    *   **SUBMIT INTERIM MILESTONE**.

*   **Tue Feb 17**: **Sprint 5 - Final Polish**
    *   Add Docker support (`Dockerfile` + `docker-compose.yml`).
    *   Finalize documentation and architecture diagrams.
    *   Submit Final Capstone Project.
