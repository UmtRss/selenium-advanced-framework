# Selenium Advanced Framework with GitHub Actions CI

This project is an advanced Selenium + PyTest automation framework with CI integration using GitHub Actions.

## 🚀 Features
- ✅ Page Object Model (POM) structure
- ✅ Selenium + PyTest integration
- ✅ GitHub Actions CI pipeline (automatic test run on push)
- ✅ Headless Chrome setup for CI
- ✅ Example working login test (`the-internet.herokuapp.com`)

## 📂 Project Structure
selenium-advanced-framework/
├── .github/workflows/ci.yml # CI pipeline config
├── pages/login_page.py # POM: Login page object
├── tests/test_login.py # Test: Valid login test
├── conftest.py # PyTest fixture: Selenium WebDriver
├── requirements.txt # Python dependencies
└── README.md # Project description


## ⚙️ How to Run Locally
1️⃣ Install dependencies:
```bash
pip install -r requirements.txt

pytest --disable-warnings --tb=short

