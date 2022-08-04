from pageObjects.loginPage import LoginPage
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#__________________________________________________________________#

# setup code for calling browser of our choice. by using following command
# pytest -s -v -n=2 testCases/test_login.py --browser chrome
# Instead of Chrome we can mention firefox as well
# and if we do not specify any browser then by default it will launch Microsoft Edge driver.

@pytest.fixture()
def setup(browser):               # setup method
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching FireFox Browser........")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching MicroSoft Edge Browser........")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome Browser........")
    return driver

def pytest_addoption(parser):      # this will get the value from CLI (command line Interface) / hooks
    parser.addoption("--browser")  # i.e. It will read browser name which we will mention in the terminal window

@pytest.fixture()
def browser(request):              # This will return the browser value to setup method.
    return request.config.getoption("--browser")

#_________________________________________________________________________#

## setup Code for launching Chrome Driver only.

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver


#____________________________________________________________________________#
#______________ Pytest HTML Report __________________________________________#

# to generate HTML report we need to give following command in terminal window
# pytest -s -v --html=Reports\report.html testCases/test_login.py
# we can mention specific browser name as well.
# pytest -s -v --html=Reports\report.html testCases/test_login.py --browser chrome

# Hook for adding environment into HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'customer'
    config._metadata['tester'] = 'Shoeb'

# Hook for deleting/modifying environment into HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

