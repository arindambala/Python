# Day 52 - 100 Days of Code

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from dotenv import load_dotenv
from time import sleep

print(f'\n---- Follow ^ Bot ----\n')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_path)

URL = os.getenv('STALK_URL')
BASE_URL = os.getenv('ACCOUNT_URL')
MAIL = os.getenv('IG_MAIL')
PASSWORD = os.getenv('IG_KEY')
LOGIN_URL = f'{BASE_URL}/login'

class IgFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
    def log_in(self):
        self.driver.get(LOGIN_URL)
        
        try:
            decline = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Decline")]')))
            decline.click()
        except TimeoutException:
            pass
        
        username = self.wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        password = self.driver.find_element(By.NAME, 'password')
        
        username.send_keys(MAIL)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        
        try:
            save_info = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Not now")]')))
            save_info.click()
        except TimeoutException:
            pass
        
        try:
            notifs = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not now")]')))
            notifs.click()
        except TimeoutException:
            pass
        
    def find_followers(self):
        self.driver.get(f'{BASE_URL}/u/{URL}/followers')
        
        modal = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.followers-scroll')))
        
        for _ in range(10):
            last_height = self.driver.execute_script('return arguments[0].scrollHeight', modal)
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            
            try:
                self.wait.until(lambda d: self.driver.execute_script('return arguments[0].scrollHeight', modal) > last_height)
            except TimeoutException:
                break
        
    def start_follow(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, '.followers-scroll button')
        
        for btn in buttons:
            try:
                self.wait.until(EC.element_to_be_clickable(btn))
                btn.click()
                
                sleep(0.5)
            except ElementClickInterceptedException:
                try:
                    cancel = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Cancel")]')))
                    cancel.click()
                except TimeoutException:
                    pass

bot = IgFollower()

bot.log_in()
bot.find_followers()
bot.start_follow()