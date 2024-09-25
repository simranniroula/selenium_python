from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome()
class DemoMultipleTabs:
    def MultipleWindows(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, "//div//section//div//img[@class='conta iner']").click()

        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//a[normalize-space()='Offers']")
                time.sleep(4)
                driver.close()
                time.sleep(3)
                break

        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//div//section//div//img[@class='conta iner']").click()
        time.sleep(4)


multipletab = DemoMultipleTabs()
multipletab.MultipleWindows()
