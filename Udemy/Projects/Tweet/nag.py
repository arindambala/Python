# Day 51 - 100 Days of Code

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

print(f'\n---- Complain ^ Bot ----\n')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_path)

URL = os.getenv('URL')
MAIL = os.getenv('TW_MAIL')
PASSWORD = os.getenv('TW_KEY')
UP = os.getenv('NET_UP')
DOWN = os.getenv('NET_DOWN')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

class InternetSpeedBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 90)
        self.up = 0
        self.down = 0
    
    def get_netspeed(self):
        self.driver.get('https://www.speedtest.net/')
        
        start_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.start-button a')))
        start_btn.click()
        
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.result-container-speed-active')))
        
        self.up = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.upload-speed'))).text
        self.down = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.download-speed'))).text
        
        print(f'Collected data : Upload - {self.up} Mbps | Download - {self.down} Mbps')
    
    def send_providertweet(self):
        self.driver.get(URL)
        
        username_field = self.wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        username_field.send_keys(MAIL)
        
        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)
        
        tweet_compose = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Post text"]')))
        
        tweet = f'Excuse me, what in the scam is going on here? Why is my upload speed {self.up} Mbps & download speed {self.down} Mbps, instead of - upload speed {UP} Mbps & download speed {DOWN} Mbps? Care to explain bruv?!'
        tweet_compose.send_keys(tweet)
        
        tweet_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.x-compose-form button')))
        tweet_btn.click()
        
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.x-compose-form button')))
        self.driver.quit()

bot = InternetSpeedBot()

bot.get_netspeed()
bot.send_providertweet()