# Implementation Plan: Week 11 (Brent Oil) Productionization

## Goal
My goal is to transform the "Brent Oil Price Change Point Analysis" from a research prototype into a **Production-Grade Fintech Application** by Week 12 standards.

## User Review Required
> [!IMPORTANT]
> This plan involves significant refactoring of the `backend` to introduce Type Hints and Dataclasses. This might temporarily break the frontend if API responses change format. I will ensure backward compatibility or update the frontend concurrently.

## Sprints

### Sprint 1: Reliability Foundation & Testing
**Focus**: Establish a safety net with comprehensive testing.
- [ ] **Setup Test Infrastructure**: Install `pytest`, `pytest-cov`.
- [ ] **Unit Tests**:
    - [ ] Create `backend/tests/test_services.py` to test data loading and processing logic (mocking file I/O).
    - [ ] Create `backend/tests/test_models.py` if custom model classes exist.
- [ ] **Integration Tests**:
    - [ ] Create `backend/tests/test_api.py` to verify Flask endpoints return correct status codes and data structures.
    - [ ] Verify `frontend` builds and renders (basic smoke test).

### Sprint 2: Engineering Excellence
**Focus**: Improve code quality, readability, and maintainability.
- [ ] **Type Hints**:
    - [ ] Add Python type annotations to all functions in `backend/app/services.py` and `routes.py`.
    - [ ] configuring `mypy` to enforce typing standards.
- [ ] **Logging**:
    - [ ] Replace `print()` statements with structured `logging`.
    - [ ] Configure log rotation and formatting in `backend/app/__init__.py`.
- [ ] **Dataclasses**:
    - [ ] Refactor raw dictionary data passing into `dataclasses` (e.g., `PricePoint`, `Event`, `ChangePoint`).

### Sprint 3: CI/CD Pipeline
**Focus**: Automate quality assurance.
- [ ] **Upgrade CI Workflow**:
    - [ ] Update `.github/workflows/ci.yml`.
    - [ ] Add steps to install test dependencies.
    - [ ] Add `pytest` execution step with failure thresholds.
    - [ ] Add `mypy` type checking step.
- [ ] **Pre-commit Hooks** (Optional but recommended):
    - [ ] Setup `pre-commit` for local linting before push.

### Sprint 4: Explainability & Insights
**Focus**: Demystify the "Black Box" model for users.
- [ ] **Model Transparency**:
    - [ ] Improve the `/api/changepoint/trace` endpoint to return more granular posterior data.
    - [ ] (Optional) Implement a basic SHAP implementation if the model allows, or enhanced visualization of the MCMC trace.
- [ ] **Contextual Explanations**:
    - [ ] Add a new endpoint that generates natural language summaries of the change points (e.g., "75% probability change driven by [Event]").

### Sprint 5: Deployment Readiness & Polish
**Focus**: Prepare for "The Real World".
- [ ] **Dockerization**:
    - [ ] specific `Dockerfile` for Backend.
    - [ ] specific `Dockerfile` for Frontend.
    - [ ] `docker-compose.yml` to orchestrate both services + database (if needed).
- [ ] **Documentation**:
    - [ ] Update `README.md` with "How to Run Tests" and "Architecture Diagram".
    - [ ] Add badges for Build Status and Code Coverage.

## Verification Plan

### Automated Tests
- Run `pytest backend/tests` to verify backend logic.
- Run `npm test` in `frontend` (if available) or build check `npm run build`.
- Check GitHub Actions run for green status.

### Manual Verification
- **Dashboard Check**: Launch the full stack (`backend` + `frontend`) and verify charts render.
- **API Check**: Use `curl` or Postman to hit endpoints and verify JSON structure matches new Dataclasses.
