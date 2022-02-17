from selenium install webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestOne:

    def test_e2e(self, setup):


        setup.driver.find_element_by_css_selector("a[href*='shop']").click()
        cards = self.driver.find_elements_by_css_selector(".card-title a")
        i = -1
