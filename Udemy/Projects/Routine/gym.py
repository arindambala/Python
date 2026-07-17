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

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(GYM_URL)

wait = WebDriverWait(driver, 10)

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

cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

target_ids = []

for card in cards:

    card_id = card.get_attribute('id').replace('class-card-', '')

    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id,'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    time_text = card.find_element(By.ID, f'class-time-{card_id}').text

    if (("tue" in day_title.lower() or "thu" in day_title.lower()) and "6:00 PM" in time_text):
        target_ids.append(card_id)

print(f"\nFound {len(target_ids)} Tuesday/Thursday 6 PM classes.\n")

booked_count = 0
waitlist_count = 0
already_booked_count = 0

for card_id in target_ids:

    try:
        card = driver.find_element(By.ID, f'class-card-{card_id}')
    except Exception:
        print(f'Skipping missing card: {card_id}')
        continue
    
    class_name = card.find_element(By.ID, f'class-name-{card_id}').text
    
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id,'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, 'h2').text

    try:
        book_btn = card.find_element(By.ID, f'book-button-{card_id}')
    except NoSuchElementException:
        print(f'Already booked or unavailable: {class_name} ({day_title})')
        already_booked_count += 1
        continue

    btn_text = book_btn.text.strip()

    print(f"Checking {class_name} | {day_title} | {btn_text}")

    if btn_text == 'Booked':
        already_booked_count += 1
        print('✔ Already booked.')
    elif btn_text == 'Waitlisted':
        already_booked_count += 1
        print('✔ Already waitlisted.')
    elif btn_text == 'Book Class':
        book_btn.click()
        wait.until(lambda d: d.find_element(By.ID, f'book-button-{card_id}').text.strip() == 'Booked')
        booked_count += 1
        print('✅ Successfully booked.')
    elif btn_text == 'Join Waitlist':
        book_btn.click()
        wait.until(lambda d: d.find_element(By.ID, f'book-button-{card_id}').text.strip() == 'Waitlisted')
        waitlist_count += 1
        print('✅ Joined waitlist.')

expected_count = len(target_ids)

print(f'\n_---- Total TUESDAY or THURSDAY 6 PM Classes : {expected_count} ----_')
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
            print(f'\n✔ Verified : {class_name} ({when_text})')
            verified_count += 1
    except NoSuchElementException:
        pass

print('\n\n_---- VERIFICATION RESULT ----_\n')

print(f'Expected bookings : {expected_count}')
print(f'Found bookings    : {verified_count}')

if expected_count == verified_count:
    print('\n✅ SUCCESS : All Tuesday/Thursday 6 PM classes are booked!')

else:
    print(f'\n❌ Expected {expected_count} bookings but found {verified_count}.')

driver.quit()