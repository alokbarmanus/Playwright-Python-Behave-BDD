## CI/CD Integration Example

If you use a CI/CD tool (like GitHub Actions, Jenkins, or Azure DevOps), add a step after your test execution to generate the Allure report:

```
allure generate allure-results -o allure-report --clean
```

Then archive or publish the allure-report folder as an artifact.
## Test Reporting

### Allure Report
1. Run your tests with Allure formatter:
  ```
  behave -f allure_behave.formatter:AllureFormatter -o allure-results
  ```
2. Generate the Allure HTML report (requires Allure CLI):
  ```
  allure generate allure-results -o allure-report --clean
  allure open allure-report
  ```

### Behave HTML Formatter (built-in)
Run your tests with the HTML formatter:
```
behave -f html -o behave-report.html
```

The HTML report will be generated as `behave-report.html` in your project directory.
# Playwright Python Behave BDD Automation Framework

This project is an industry-standard automation framework using Playwright, Python, and Behave for BDD. It follows the Page Object Model (POM) pattern and is structured for maintainability and scalability.

## Folder Structure

- features/
  - steps/                # Step definitions for Behave
  - pages/                # Page Object classes (locators & functions)
  - utilities/            # Utility classes
  - environment.py        # Behave hooks for setup/teardown
  - login.feature         # Sample login scenarios
- tests/
  - base_test.py          # Base test class for browser setup/teardown
  - base_page.py          # Base page class for common page actions
- configs/
  - application.properties # App URL, browser, retry count, wait
- README.md

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run tests:
   ```bash
   behave
   ```

## Sample Login Scenario
- Navigate to https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username and password
- Click Login
- Verify successful login

---

Replace placeholders and extend as needed for your application.