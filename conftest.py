import pytest
from selenium install webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pytest_addoption(parser):
    parser.addoption(
        "--browser_Name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getOption("browser_name")
    if browser_name == "chrome":
        ser = Service('C:\WebDriver\Bin\chromedriver.exe')
        op = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=ser, options=op)
    elif browser_name == "firefox":
        # write firefox invocation

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()