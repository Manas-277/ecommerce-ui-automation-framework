# Ecommerce UI Automation Framework

[![CI](https://github.com/Manas-277/ecommerce-ui-automation-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/Manas-277/ecommerce-ui-automation-framework/actions)

A clean, lightweight Selenium + Pytest framework for end-to-end UI automation of [SauceDemo](https://www.saucedemo.com/).  
Built with Page Object Model, parallel execution, HTML reporting, failure screenshots, and GitHub Actions CI.

---

## Highlights

- Page Object Model for maintainable UI automation
- Positive and negative test coverage
- Parallel execution with `pytest-xdist`
- HTML report generation with `pytest-html`
- Automatic screenshots on failure
- GitHub Actions pipeline on every push to `main`
- Headless execution support for CI


## Tech Stack

- Python 3.12+
- Selenium
- Pytest
- pytest-xdist
- pytest-html
- GitHub Actions

---

## Project Structure

```text
.
├── pages/
├── tests/
├── reports/
│   ├── html/
│   └── screenshots/
├── .github/
│   └── workflows/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Test Coverage

### Positive
- Valid login
- Add item to cart
- Checkout flow
- Logout

### Negative
- Invalid login
- Empty login fields
- Empty checkout fields

### End-to-End
- Login → add product → cart → checkout → finish → logout

---

## Setup

```bash
git clone <repo-url>
cd ecommerce-ui-automation-framework
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## Run Tests

```bash
pytest
```

---

## Run in Parallel

```bash
pytest -n auto
```

---

## Generate HTML Report

The HTML report is generated in:

```text
reports/html/report.html
```

---

## Failure Screenshots

If a test fails, a screenshot is saved under:

```text
reports/screenshots/
```

---

## GitHub Actions

The CI workflow runs on push to `main` and executes the full Pytest suite automatically.

---

## Future Scope

- Cross-browser execution
- Retry logic for flaky tests
- Allure reporting
- Data-driven testing
- Dockerized execution
