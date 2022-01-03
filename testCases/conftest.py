from selenium import webdriver
from Utilities.ExcelUtils import ExcelUtils
import pytest
import os

from datetime import date
import sys

sys.dont_write_bytecode = True
today = date.today().strftime("%d-%m-%Y")

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox
    else:driver=webdriver.Chrome()
    if os.path.isdir(".\\Screenshots\\" + today):
        pass
    else:
        os.makedirs(".\\Screenshots\\" + today)
    return driver
@pytest.fixture()
def login_excel_data():
    excel=ExcelUtils(".\\TestData\\TestData.xlsx")

    return excel


def pytest_addoption(parser): # this will get value from command prompt terminal, we call it as hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #this will return the browser value to setup method
    return request.config.getoption("--browser")

########## pytest HTMl Reports############
#it is hook for adding Enviornmental info to HTML reports
def pytest_configure(config):
    config._metadata['Project Name']= 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JVA_HOME", None)
    metadata.pop("Plugins",None)
