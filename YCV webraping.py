import requests
from bs4 import BeautifulSoup
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36}'}
url = 'https://youthcentervratza.com'
r = requests.Session()
html = r.get(url=url,headers=headers).text
doc = BeautifulSoup(html, 'html.parser')
descriptions = []
titles = []
news_length = len(doc.find_all(class_='service_item_content')[1])
for i in range(0, news_length+1):
    description = doc.find_all(class_='service_item_content')[i].p.text
    descriptions.append(description)
for i in range(0, news_length+1):
    title = doc.find_all(class_='service_item_content')[i].find(class_='service_item_title').text
    link = doc.find_all(class_='service_item_content')[i].find(class_='button service_item_button trans_200').a['href']
    titles.append(title)
    print(f'{i+1} {descriptions[i]} {link}')




