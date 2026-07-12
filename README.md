# Ecommerce Test Automation Framework

A Selenium WebDriver + PyTest automation framework developed using Python following the Page Object Model (POM) design pattern.

## Technologies Used

- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- WebDriver Manager
- HTML Reports
- Logging
- Git & GitHub

---

## Project Structure

```
Ecommerce-Test-Automation-Framework
│
├── config
├── data
├── logs
├── pages
├── reports
├── screenshots
├── tests
├── utilities
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Features

- Page Object Model (POM)
- BasePage for reusable Selenium methods
- Explicit Waits
- Dynamic Test Data Generation
- Logging
- Screenshot Capture on Test Failure
- HTML Test Reports
- Config File Support
- Reusable PyTest Fixtures

---

## Automated Test Scenarios

- Launch Application
- User Registration
- Complete User Registration
- Verify Account Created
- Continue After Registration
- Delete Account
- Verify Account Deleted
- Login Page Navigation

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

Generate HTML Report:

```bash
pytest --html=reports/report.html
```

---

## Framework Highlights

- Selenium WebDriver with Python
- PyTest Test Framework
- Page Object Model
- Reusable BasePage methods
- Config-driven framework
- Dynamic test data generation
- HTML Reporting
- Logging
- Screenshot capture on failures

---

## Author

Gokul S

## Sample Test Flow

User Registration

Launch Browser

↓

Open Automation Exercise

↓

Register New User

↓

Fill Registration Form

↓

Create Account

↓

Verify Account Created

↓

Continue

↓

Delete Account

↓

Verify Account Deleted

↓

Close Browser

## Sample Report

HTML Report

![HTML Report](reports/report.png)

---

## Failure Screenshot

![Failure Screenshot](screenshots/sample.png)