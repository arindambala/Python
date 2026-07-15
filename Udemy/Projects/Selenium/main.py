# Day 48 - 100 Days of Code

from selenium import webdriver
from selenium.webdriver.common.by import By

print(f'\n---- Selenium ^ WebDriver ----\n')

# Configure web driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.in/8Bitdo-Ultimate-Controller-Joysticks-Remappable/dp/B0D72RVDLH/')

price = driver.find_element(By.CLASS_NAME, value='a-price-whole')
print(f'8bitdo Ultimate 2C controller price : {price.text}')

chauffeur = webdriver.Chrome(chrome_options)
chauffeur.get('https://www.python.org/')

search_bar = chauffeur.find_element(By.NAME, value='q')
print(f'\n{search_bar}\n{search_bar.tag_name}\n{search_bar.get_attribute('placeholder')}')

button = chauffeur.find_element(By.ID, 'submit')
print(f'\n{button}\n{button.size}')

doc_link = chauffeur.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
print(f'\n{doc_link}\n{doc_link.text}')

bug_link = chauffeur.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(f'\n{bug_link}\n{bug_link.text}')

# Extract Data
event_times = chauffeur.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = chauffeur.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

events = {
    num: {
        'time': time_el.text,
        'name': name_el.text,
    }
    for num, (time_el, name_el) in enumerate(zip(event_times, event_names))
}
print(events)

'''
event = {}

for num in range(len(event_times)):
    event[num] = {
        'time': event_times[num].text,
        'name': event_names[num].text,
    }
print(event)
'''

# driver.close() # Closes Tabs
driver.quit() # Closes Browser
chauffeur.quit()