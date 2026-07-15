# Day 48 - 100 Days of Code

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element(By.ID, value='mwDw')
# print(article_count.text)

all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()

search_bar = driver.find_element(By.NAME, value='search') 
search_bar.send_keys('Python', Keys.ENTER)

# Forms
chauffeur = webdriver.Chrome(options=chrome_options)
chauffeur.maximize_window()
chauffeur.get('https://appbrewery.github.io/fake-newsletter-signup/')

first_name = chauffeur.find_element(By.NAME, value='fName')
last_name = chauffeur.find_element(By.NAME, value='lName')
email_id = chauffeur.find_element(By.NAME, value='email')
button = chauffeur.find_element(By.XPATH, value='//*[@id="signup-form"]/button')

first_name.send_keys('Test1')
last_name.send_keys('Test2')
email_id.send_keys('Test3@mail.test')
button.click()

driver.quit()
chauffeur.quit()