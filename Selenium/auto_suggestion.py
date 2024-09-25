from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome()
class DemoAutoSuggestion:
    def auto_suggestion(self):
        driver = webdriver.Chrome()
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        # self.driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://www.yatra.com/")

        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(2)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        time.sleep(2)
        going_to.send_keys("New York")
        time.sleep(4)

        search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for results in search_result:
            print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(4)
                break


search = DemoAutoSuggestion()
search.auto_suggestion()
