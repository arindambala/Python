# Day 45 - 100 Days of Code

from bs4 import BeautifulSoup
import requests

print(f'\n---- Top 100 ^ Movies ----\n')

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
response.raise_for_status()

website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser') # print(soup.prettify())

movies = soup.find_all(name='h3', class_='title')
# print(movies)

if len(movies) == 0:
    print('❗ Scraper got no titles!')
else:
    movie_titles = [movie.getText() for movie in movies]
    movies_list = movie_titles[::-1]
    # print(movies_list)
    
    with open('scrap.txt', mode='w', encoding='utf-8') as file:
        file.write('\n'.join(movies_list))
    print('✅ Text file successfully created!')