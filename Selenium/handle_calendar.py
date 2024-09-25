from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome()
class DemoAutoSuggestion:
    def auto_suggestion(self):
        driver = webdriver.Chrome()
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
            # print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(4)
                break
            time.sleep(4)
# Handle Calendar
        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(4)
        # driver.find_element(By.XPATH, "//td[@id='26/09/2024']").click()
        # time.sleep(4)

        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "30/09/2024":
                date.click()
                time.sleep(4)
                break


search = DemoAutoSuggestion()
search.auto_suggestion()
