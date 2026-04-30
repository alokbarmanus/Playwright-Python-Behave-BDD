#!/bin/bash
# Activate virtual environment if it exists
if [ -d ".venv" ]; then
  source .venv/bin/activate
fi

# Set ENV variable from argument or default to dev
env_arg=${1:-dev}
export ENV="$env_arg"
echo "Running tests in ENV: $ENV"

# Run Behave with Allure formatter, parallel execution, and no capture
behave -D ENV=$ENV --tags=@regression --no-capture -f allure_behave.formatter:AllureFormatter -o allure-results --processes 4 --parallel-element scenario

# Generate Allure HTML report (requires Allure CLI installed)
allure generate allure-results -o allure-report --clean
# Optionally open the report (uncomment if needed)
# allure open allure-report
