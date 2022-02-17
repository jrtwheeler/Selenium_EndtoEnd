import pytest
from selenium install webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="class")
def setup():
    ser = Service('C:\WebDriver\Bin\chromedriver.exe')
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    yield
    driver.close()
    return driver