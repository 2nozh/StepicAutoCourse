import time
import os
import math
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def task_1_6(html):
    try:
        driver.get(html)
        driver.find_element(By.CSS_SELECTOR, '.first_block input[class="form-control first"]').send_keys("myname")
        driver.find_element(By.CSS_SELECTOR, '.first_block input[class="form-control second"]').send_keys("mylastname")
        driver.find_element(By.CSS_SELECTOR, '.first_block input[class="form-control third"]').send_keys("email")
        driver.find_element(By.CSS_SELECTOR, '.second_block input[class="form-control first"]').send_keys("12345")
        driver.find_element(By.CSS_SELECTOR, '.second_block input[class="form-control second"]').send_keys("address")
        driver.find_element(By.CSS_SELECTOR, "button").click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        driver.quit()
def task_2_1_5():
    driver.get("https://suninjuly.github.io/math.html")
    x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, "button").click()


def task_2_1_7():
    driver.get("http://suninjuly.github.io/get_attribute.html")
    x = driver.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex")
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, "button").click()
    print(x)


def task_2_2_3():
    driver.get("https://suninjuly.github.io/selects2.html")
    num1 = driver.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = driver.find_element(By.CSS_SELECTOR, "#num2").text
    sum = int(num1) + int(num2)
    select_element = Select(driver.find_element(By.CSS_SELECTOR, "#dropdown"))
    select_element.select_by_value(str(sum))
    driver.find_element(By.CSS_SELECTOR, "button").click()


def task_2_2_6():
    driver.get("https://suninjuly.github.io/execute_script.html")
    x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    checkbox = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
    driver.execute_script("return arguments[0].scrollIntoView(true)", checkbox)
    checkbox.click()
    driver.find_element(By.CSS_SELECTOR, "button").click()

def task_2_2_8():
    driver.get("https://suninjuly.github.io/file_input.html")
    driver.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys("myname")
    driver.find_element(By.CSS_SELECTOR, 'input[name="lastname"]').send_keys("mylastname")
    driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("email")
    dir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(dir, 'file.txt')
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(path)
    driver.find_element(By.CSS_SELECTOR, "button").click()

def task_2_3_4():
    driver.get("http://suninjuly.github.io/alert_accept.html")
    driver.find_element(By.CSS_SELECTOR, "button").click()
    confirm = driver.switch_to.alert
    confirm.accept()
    x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, "button").click()

def task_2_3_6():
    driver.get("http://suninjuly.github.io/redirect_accept.html")
    driver.find_element(By.CSS_SELECTOR,"button").click()
    driver.switch_to.window(driver.window_handles[1])
    x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, "button").click()


def task_2_4_8():
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    button = WebDriverWait(driver,30).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#price"),"$100")
    )
    driver.find_element(By.CSS_SELECTOR, "button").click()
    x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, "button#solve").click()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options)
    task_1_6("https://suninjuly.github.io/registration1.html")
