# Day 45 - 100 Days of Code

from bs4 import BeautifulSoup
# import lxml

print(f'\n---- Beautiful ^ Soup ----\n')

with open(file='index.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser') # 'lxml' for certain websites
print(soup.title)
print(f'\nName : {soup.title.name} | String : {soup.title.string}\n')

# print(soup)
# print(soup.prettify())

anchor_tags = soup.find_all(name='a') # soup.a
# print(anchor_tags)
for tag in anchor_tags:
    print(tag.getText())
    # print(tag.get('href'))

heading = soup.find(name='h1', id='name')
print(f'\n{heading}')

section = soup.find(name='h3', class_='heading') # 'class' - Reserved keyword | _ to not clash with py
print(f'\n{section}\nText : {section.getText()}\nName : {section.name}\nAttribute : {section.get('class')}\n')

company_url = soup.select_one(selector='p a') # Returns the first match | CSS Selector
print(f'\n{company_url}')

name = soup.select_one(selector='#name')
print(f'\n{name}')

class_ = soup.select_one(selector='.heading')
print(f'\n{class_}')

class_all = soup.select('.heading')
print(f'\n{class_all}')