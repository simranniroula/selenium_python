from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class DemoFindElementBySelector():
    def locate_by_selector(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(4)
        #       driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("test@test.com")
        lista = driver.find_elements(By.TAG_NAME, 'a')
        print(len(lista))
        # for i in lista:
        #     print(i.text)

        text = driver.find_element(By.XPATH, "//a[@id='booking_engine_flights']").text
        print("Fetched Text: " +text)
        time.sleep(2)
        text1 = driver.find_element(By.LINK_TEXT, "Yatra for Business").text
        print(text1)
        time.sleep(2)

        # Get Element Attribute Value
        attr_value = driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("type")
        print(attr_value)


findelement = DemoFindElementBySelector()
findelement.locate_by_selector()

"""
class DemoSeleniumLearning():
    def demo_browser_methods(self):
        driver = webdriver.Chrome()
        driver.get("https://training.rcvacademy.com/")
        print(driver.current_url)
        time.sleep(5)
        print(driver.title)
        driver.maximize_window()
        time.sleep(5)
#       driver.fullscreen_window()
        driver.refresh()
        time.sleep(7)
        driver.find_element(By.LINK_TEXT, 'ALL COURSES').click()
        time.sleep(5)
        driver.back()
        time.sleep(5)
        driver.forward()
        time.sleep(5)
        driver.minimize_window()
        time.sleep(5)
        driver.quit()


demobrowser = DemoSeleniumLearning()
demobrowser.demo_browser_methods()
"""

