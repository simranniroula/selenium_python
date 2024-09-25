from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class JsExecution():
    def demo_javascript(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.get("https://training.rcvacademy.com/")
        driver.execute_script("window.open('https://training.rcvacademy.com/', '_self');")
        time.sleep(6)
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();", demo_element)


demojs = JsExecution()
demojs.demo_javascript()
