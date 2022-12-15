import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
buttonBook = browser.find_element(By.ID, "book")
buttonBook.click()
x_element = int(browser.find_element(By.ID, "input_value").text)
x = calc(x_element)
inputField = browser.find_element(By.ID, "answer").send_keys(x)
buttonSubmit = browser.find_element(By.ID, "solve").click()

time.sleep(5)
browser.quit()
