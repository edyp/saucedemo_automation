import os
import sys
import json
from pathlib import Path
import pytest
from selenium import webdriver
from common.logger import Logger
from pages.login_page import LoginPage


LOG = Logger()
def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='chrome',
        help='Choose browser you have on your machine.',
        choices=('chrome', 'firefox', 'safari')
    )

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')

def driver_provider(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    else:
        driver = webdriver.Safari()
    return driver

@pytest.fixture(scope='session')
def driver(browser):
    driver = driver_provider(browser)
    yield driver
    driver.close()

def concat_static_file_path(file_name):
    rootdir = str(Path().resolve()).replace('tests', '')
    new_json_file_path = ['common', 'static', file_name]
    return os.path.join(rootdir, *new_json_file_path)

def pytest_sessionstart(session):
    """This hook define environment setup and cleanning procedure before
    collecting tests for session.
    """
    # Session setup
    LOG.info(10*'#'+' Preparing envirnoment for session '+10*'#')
    LOG.info(18*'#'+f' BROWSER: {session.config.option.browser} '+18*'#')
    driver = driver_provider(session.config.option.browser)
    path = concat_static_file_path('default_credentials.json')
    credentials = LoginPage(driver).get_credentials()
    driver.close()
    # Create a json file with all default credentials
    with open(path, 'w+') as json_f:
        json.dump(credentials, json_f, indent=4)

    try:
        assert Path(path).is_file()
        assert Path(path).stat().st_size > 0
    except AssertionError:
        pytest.exit(f'File {path} necessary for running tests doesn\'t exist'
                    + ' or is empty.')
    LOG.info(17*'#'+' Environment ready! '+18*'#')

def pytest_sessionfinish(session, exitstatus):
    # Session teardown cleanning
    path = concat_static_file_path('default_credentials.json')
    Path(path).unlink(missing_ok=True)
    LOG.info(17*'#'+' Environment clean! '+18*'#')
