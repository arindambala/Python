# Day 45 - 100 Days of Code

from bs4 import BeautifulSoup
import requests

print(f'\n---- Web ^ Scrap ----\n')

response = requests.get('https://news.ycombinator.com/news') # Always check - /robots.txt
response.raise_for_status()

yc_web = response.text # print(response.text)

soup = BeautifulSoup(yc_web, 'html.parser')
# print(soup.title)

# Basic
'''
titles = soup.select('.titleline > a')
print(f'---- Found {len(titles)} Titles ----\n')

for index, title in enumerate(titles, start=1):
    print(f'{index}. {title.getText()}')
'''

# Advanced
'''
title_lines = soup.find_all(class_='titleline')
print(f'---- Found {len(title_lines)} Titles ----\n')

for index, anchor in enumerate(title_lines, start=1):
    title_link = anchor.find('a')
    if title_link:
        title_text = title_link.getText()
        print(f'{index}. {title_text}')
'''

title_tag = soup.find_all(name='span', class_='titleline')
article_texts = []
article_links = []
article_upvotes = []

for span_tag in title_tag:
        article_tag = span_tag.find('a')
        if article_tag:
            text = article_tag.getText()
            article_texts.append(text)
            
            link = article_tag.get('href')
            article_links.append(link)
            
            score_text = span_tag.find_parent('tr').find_next_sibling('tr')
            score_found = score_text.find(name='span', class_='score')
            if score_found:
                points = int(score_found.getText().split()[0])
                article_upvotes.append(points)
            else:
                article_upvotes.append(0)

print(f'Texts : {article_texts}\n')
print(f'Links : {article_links}\n')
print(f'Scores : {article_upvotes}\n')

max_upvotes = max(article_upvotes)
index_max = article_upvotes.index(max_upvotes)

print(f'Popular Upvote : {index_max} | Upvotes : {max_upvotes}')
print(f'Popular Text : {article_texts[index_max]}')
print(f'Popular Link : {article_links[index_max]}')