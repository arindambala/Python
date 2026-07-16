# Day 49 - 100 Days of Code

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import time

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
time.sleep(2)

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

booked_count, waitlist_count, already_booked_count = 0, 0, 0
total_count = 0

classes = []

for i in range(len(class_cards)):
    curr_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
    card = curr_cards[i]
    
    card_id = card.get_attribute('id').replace('class-card-', '')
    
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, 'h2').text
    
    if 'Tue' in day_title or 'Thu' in day_title:
        time_text = card.find_element(By.ID, f'class-time-{card_id}').text
        
        if '6:00 PM' in time_text:
            class_name = card.find_element(By.ID, f'class-name-{card_id}').text
            
            book_btn = card.find_element(By.ID, f'book-button-{card_id}')
            
            class_info = f'{class_name} on {day_title}'
            btn_text = book_btn.text.strip()
            
            if btn_text == 'Booked':
                print(f'❗ Already Booked : {class_name} on {day_title} !')
                already_booked_count += 1
                classes.append(f'[Booked] {class_info}')
            elif btn_text == 'Waitlisted':
                print(f'❗ Already Waitlisted : {class_name} on {day_title} !')
                already_booked_count += 1
                classes.append(f'[Waitlisted] {class_info}')
            elif btn_text == 'Book Class':
                book_btn.click()
                print(f'✅ Successfully Booked : {class_name} on {day_title} !')
                booked_count += 1
                classes.append(f'[New Booking] {class_info}')
                time.sleep(1.5)
            elif btn_text == 'Join Waitlist':
                book_btn.click()
                print(f'✅ Joined Waitlist : {class_name} on {day_title} !')
                waitlist_count += 1
                classes.append(f'[New Waitlist] {class_info}')
                time.sleep(1.5)

total_count = booked_count + waitlist_count + already_booked_count

print(f'\n_---- Total TUESDAY or THURSDAY 6 PM Classes : {total_count} ----_')
print(f'\n\n....VERYFYING BOOKINGS PAGE....')

bookings_link = driver.find_element(By.ID, 'my-bookings-link')
bookings_link.click()

wait.until(EC.presence_of_element_located((By.ID, 'my-bookings-page')))

verified_count = 0

cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in cards:
    try:
        when_para = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_para.text
        
        if ('Tue' in when_text or 'Thu' in when_text) and '6:00 PM' in when_text:
            class_name = card.find_element(By.TAG_NAME, 'h3').text
            print(f'\n✔ Verified : {class_name}')
            verified_count += 1
    except NoSuchElementException:
        pass

print(f'\n\n_---- VERIFICATION RESULT ----_\n')
print(f'Expected bookings : {total_count}')
print(f'Found bookings : {verified_count}')

if total_count == verified_count:
    print('\n✅ SUCCESS : All bookings verified!')
else:
    print(f'\n❌ MISMATCH : Missing {total_count - verified_count} bookings!')

driver.quit()