import requests

from bs4 import BeautifulSoup

packet=list(range(18))

 
def KCRuliweb():

    global packet
    
    url = 'https://www.ruliweb.com/' # DataLab의 주소.

     

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    webpage = requests.get(url,headers=headers)

    soup = BeautifulSoup(webpage.content, "html.parser")




    #print(soup)

    li = soup.find_all('div', class_="col col_3") # span태그의 item_title 이라는 클래스를 추출하여 result 리스트에 넣는다.

    
    result = li[1].find_all('a', class_="block")


    for i in range(len(result)):
        print(i+1,'. ',result[i].get_text(),sep='') # 검색어 출력
        packet[i]=result[i].get_text()

    

    return packet
