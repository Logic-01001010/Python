import requests
from bs4 import BeautifulSoup


url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
webpage = requests.get(url,headers=headers)
soup = BeautifulSoup(webpage.content, "html.parser")


result = soup.find_all('span', class_="item_title")



for i in range(len(result)):
    print(i+1,'. ',result[i].get_text(),sep='')


