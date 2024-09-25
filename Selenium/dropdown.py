from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()


class DemoSingleDropdown():
    def single_dropdown(self):
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        dropdown = driver.find_element(By.CSS_SELECTOR, "#dropdown-class-example")
        # time.sleep(4)
        # dropdown = driver.find_element(By.TAG_NAME, "option")
        dd = Select(dropdown)
        time.sleep(4)

        dd.select_by_index(1)
        time.sleep(4)
        dd.select_by_visible_text("Option2")
        time.sleep(4)
        dd.select_by_value("option3")
        time.sleep(4)


dd_demo = DemoSingleDropdown()
dd_demo.single_dropdown()


#   MULTISELECT DROPDOWN

