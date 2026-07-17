# Day 50 - 100 Days of Code

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from dotenv import load_dotenv

print(f'\n---- Swipe ^ Bot ----\n')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_path)

URL = os.getenv('URL')
MAIL = os.getenv('FB_MAIL')
PASSWORD = os.getenv('FB_KEY')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(URL)

wait = WebDriverWait(driver, 10)

log_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Log in']")))
log_in.click()

bark_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-facebark')))
bark_btn.click()

wait.until(lambda d: len(d.window_handles) > 1)

base_window = driver.window_handles[0]
bark_window = driver.window_handles[1]
driver.switch_to.window(bark_window)
# print(driver.title)

email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
password = driver.find_element(By.ID, 'pass')

email.send_keys(MAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

wait.until(EC.number_of_windows_to_be(1))

driver.switch_to.window(base_window)
# print(driver.title)

allow_location = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Allow"]')))
allow_location.click()

not_interested = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Not interested"]')))
not_interested.click()

accept_cookies = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="I Accept"]')))
accept_cookies.click()

for profile in range(20):
    try:
        like_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-like')))
        like_btn.click()
        
    except ElementClickInterceptedException:
        try:
            match_popup_close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.match-popup a')))
            match_popup_close.click()
            print("It's a match! Pop-up dismissed.")
        except TimeoutException:
            print("Click was intercepted by something else.")
    
    except TimeoutException:
        print("Like button disappeared. Out of profiles or page failed to load.")
        break

driver.quit()