# Day 49 - 100 Days of Code

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

print(f'\n---- Automate ^ Exercise ----\n')

env_path = 'Udemy/Projects/Routine/.env'
load_dotenv(dotenv_path=env_path)

EMAIL = os.getenv('MAIL')
PASSWORD = os.getenv('KEY')

GYM_URL = os.environ.get('URL')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

user_data_dir = os.path.join(os.getcwd(), 'chrome_profile')
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

log_in = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
log_in.click()

email_ipt = wait.until(EC.presence_of_element_located((By.ID, 'email-input')))
email_ipt.clear()
email_ipt.send_keys(EMAIL)

password_ipt = driver.find_element(By.ID, 'password-input')
password_ipt.clear()
password_ipt.send_keys(PASSWORD)

submit_btn = driver.find_element(By.ID, 'submit-button')
submit_btn.click()

wait.until(EC.presence_of_element_located((By.ID, 'schedule-page')))

# driver.quit()