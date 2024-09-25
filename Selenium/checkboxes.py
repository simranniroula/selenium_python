from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()


class DemoCheckboxes:

    def demo_checkbox(self):
        #      driver = webdriver.Chrome()

        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, "a[title='Non Stop Flights'] i[class='ico ico-checkbox']").click()
        time.sleep(3)
        var1 = driver.find_element(By.XPATH, "//i[@class='ico ico-checkbox ico-checkbox-checked']").is_enabled()
        print(var1)
        # driver.find_element(By.CSS_SELECTOR, "a[title='Senior Citizen Offer'] i[class='ico ico-checkbox']").click()
        # time.sleep(3)
        var2 = (driver.find_element(By.CSS_SELECTOR, "a[title='Senior Citizen Offer'] i[class='ico ico-checkbox']")
                .is_enabled())
        print(var2)


checkbox = DemoCheckboxes()
checkbox.demo_checkbox()
