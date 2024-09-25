from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome()
class DemoScreenshot:
    def screenshot(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.yatra.com/")

        driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@id='SignUpBtn']").click()
        time.sleep(4)
        # screenshot of web element
        continue_btn = driver.find_element(By.CSS_SELECTOR, "#login-continue-btn")
        continue_btn.screenshot(".\\ss.png")
        time.sleep(2)
        # screenshot of whole web page
        continue_btn.click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\Users\\simran.niroula_genes\\Documents\\Python_Selenium_tutorial\\error.png")
        driver.save_screenshot(".\\ss1.png")


ss = DemoScreenshot()
ss.screenshot()
