from selenium install webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestOne:

    def test_e2e(self):


        driver.find_element_by_css_selector("a[href*")