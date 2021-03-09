# pytest-bdd-with-selenium

## The power of Selenium with BDD in Python

An example showing the usage of pytest-bdd library used with selenium in Python. It consists of a basic DuckDuckGo search test using Page Object design pattern with HTML and XML reporting.

## Features

- Write feature files for UI testing with behaviour driven design approach (similar to cucumber)
- Generate XML and HTML reports
- Readable and manageable code using Page Object design pattern

## Installation

pytest-bdd-with-selenium requires [Python](https://www.python.org/download/releases/3.0/) to run.

Use a virtual environment (recommended)

```sh
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

Install the dependencies by

```sh
pip install -r requirements.txt
```

## Run the test

Run the sanity test either by

- Test file

```sh
# filter tests by test module
# note: feature files cannot be run directly
pytest tests/step_defs/test_web.py
```

OR

- Markers defined by '@' in the feature file

```sh
# filter tests by tags
# running by tag is typically better than running by path
pytest -k "unit"
```

Tags work just like pytest.mark. As a warning, marks must be explicitly added to “pytest.ini” starting with pytest 5.0.

# References

- pytest-bdd example: https://automationpanda.com/2018/10/22/python-testing-101-pytest-bdd/
- page object example: https://blog.testproject.io/2019/07/16/develop-page-object-selenium-tests-using-python/
