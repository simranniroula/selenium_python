from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()


class DemoFindElementBySelector():

    def locate_element(self):
        driver = webdriver.Chrome()

        '''driver.get("https://training.openspan.com/login")
        driver.maximize_window()
        time.sleep(4)
        demo_state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state)

        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("testing")
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("testing343")
        demo_state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        time.sleep(2)
        print(demo_state1)


findelement = DemoFindElementBySelector()
findelement.locate_element()
'''

        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        driver.maximize_window()
        elem = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem)
        driver.find_element(By.XPATH, "(//button[normalize-space()='Toggle Hide and Show'])[1]").click()
        elem1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem1)

demoElements = DemoFindElementBySelector()
demoElements.locate_element()


'''    def demo_is_displayed(self):
        driver.get("https://www.yatra.com/")
        driver.find_element(By.XPATH, "//span[@class='txt-ellipses flight_passengerBox travellerPaxBox']").click()
        driver.find_element(By.XPATH, "//div[@data-flightagegroup='child']//span[@class='ddSpinnerPlus']").click()
        text1 = driver.find_element(By.XPATH, "//span[@class='txt-ellipses flight_passengerBox travellerPaxBox']").text
        print(text1)



elements = DemoFindElementBySelector()
elements.demo_is_displayed()'''
