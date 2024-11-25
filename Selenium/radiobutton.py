from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()


class DemoRadiobutton:
    def demo_radiobutton(self):
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, "input[value='radio1']").click()
        time.sleep(3)
        select1 = driver.find_element(By.CSS_SELECTOR, "input[value='radio1']").is_selected()
        print(select1)
        # driver.find_element(By.CSS_SELECTOR, "input[value='radio2']").click()
        select2=driver.find_element(By.CSS_SELECTOR, "input[value='radio2']").is_selected()
        print(select2)


radiobutton = DemoRadiobutton()
radiobutton.demo_radiobutton()
