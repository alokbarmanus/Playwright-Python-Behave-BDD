import os
import platform
import sys

def generate_allure_environment(env=None):
    if not env:
        env = os.environ.get('ENV', 'dev')
    browser = os.environ.get('BROWSER', 'chromium')
    build = os.environ.get('BUILD', '1.0.0')
    author = os.environ.get('AUTHOR', 'Alok Barman')
    env_dir = os.path.join(os.getcwd(), "allure-results")
    os.makedirs(env_dir, exist_ok=True)
    env_file = os.path.join(env_dir, "environment.properties")
    with open(env_file, "w") as f:
        f.write(f"ENV={env}\n")
        f.write(f"BROWSER={browser}\n")
        f.write(f"PLATFORM={platform.system()} {platform.release()}\n")
        f.write(f"PYTHON_VERSION={platform.python_version()}\n")
        f.write(f"PROJECT=Playwright-Python-Behave-BDD\n")
        f.write(f"BUILD={build}\n")
        f.write(f"AUTHOR={author}\n")

if __name__ == "__main__":
    env_arg = sys.argv[1] if len(sys.argv) > 1 else None
    generate_allure_environment(env_arg)