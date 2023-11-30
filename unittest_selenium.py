from selenium import webdriver

import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YouTubeHomePage(unittest.TestCase):

    def test_home_page(self):
        driver = webdriver.Chrome()
        #driver.implicitly_wait(35)
        driver.maximize_window()

        #wait = WebDriverWait(driver, 10)
        #driver.set_page_load_timeout(10)
        driver.get("https://www.youtube.com/")
        driver.implicitly_wait(35)
        #element = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label,'Zaakceptuj wykorzystywanie plików cookie i innych danych do opisanych celów')]")))
        driver.find_element(By.XPATH, "//button[contains(@aria-label,'Zaakceptuj wykorzystywanie plików cookie i innych danych do opisanych celów')]").click()
        print("hehe")
        # except:
        #     print("Button Accept Cookie was not shown")

        web_page_title = "YouTube"
        self.assertEqual(driver.title, web_page_title)
        time.sleep(4)


