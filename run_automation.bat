@echo off
REM Run Behave tests in uat environment with regression tag, parallel, and Allure reporting

REM Activate virtual environment (if needed)
call .venv\Scripts\activate

REM Run Behave with Allure formatter, parallel execution, and no capture
behave -D ENV=uat --tags=@regression --no-capture -f allure_behave.formatter:AllureFormatter -o allure-results --processes 4 --parallel-element scenario

REM Generate Allure HTML report (requires Allure CLI installed)
allure generate allure-results -o allure-report --clean
allure open allure-report
