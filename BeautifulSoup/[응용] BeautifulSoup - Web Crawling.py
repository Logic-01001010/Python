import urllib.request
import requests
import random
from bs4 import BeautifulSoup
import os


url = 'https://bbs.ruliweb.com/community/board/300143/read/47689315?'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
webpage = requests.get(url,headers=headers)
soup = BeautifulSoup(webpage.content, "html.parser")



result = soup.find('img', class_='txc-image') # 클래스 검색.

print(result)


'''
for link in soup.find_all('a'): # a 태그 모두 찾기. href 추출.
    print(link.get('href')
'''


'''
for link in soup.find_all('img'): # img 태그 모두 찾기. src 추출.
    print(link.get('src'))
'''
