import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class test_task_1_6(unittest.TestCase):
    def test1(self):
        html = "http://suninjuly.github.io/registration1.html"
        try:
            options = Options()
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options)
            driver.get(html)
            driver.find_element(By.CSS_SELECTOR, '.first_block input[class="form-control first"]').send_keys("myname")
            driver.find_element(By.CSS_SELECTOR, '.first_block input[class="form-control second"]').send_keys(
                "mylastname")
            driver.find_element(By.CSS_SELECTOR, '.first_block input[class="form-control third"]').send_keys("email")
            driver.find_element(By.CSS_SELECTOR, "button").click()
            time.sleep(1)
            welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!",welcome_text,"test failed")
        except:
            self.assertTrue(False)
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            driver.quit()
    def test2(self):
        html = "http://suninjuly.github.io/registration2.html"
        try:
            options = Options()
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options)
            driver.get(html)
            driver.find_element(By.CSS_SELECTOR, '.first_block input[class="form-control first"]').send_keys("myname")
            driver.find_element(By.CSS_SELECTOR, '.first_block input[class="form-control second"]').send_keys(
                "mylastname")
            driver.find_element(By.CSS_SELECTOR, '.first_block input[class="form-control third"]').send_keys("email")
            driver.find_element(By.CSS_SELECTOR, "button").click()
            time.sleep(1)
            welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!",welcome_text,"test failed")
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            driver.quit()
def task_1_6(html):
    try:
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options)
        driver.get(html)
        driver.find_element(By.CSS_SELECTOR, '.first_block input[class="form-control first"]').send_keys("myname")
        driver.find_element(By.CSS_SELECTOR, '.first_block input[class="form-control second"]').send_keys("mylastname")
        driver.find_element(By.CSS_SELECTOR, '.first_block input[class="form-control third"]').send_keys("email")
        driver.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(1)
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        driver.quit()


if __name__ == '__main__':
    unittest.main()
