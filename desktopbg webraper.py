from bs4 import BeautifulSoup
import requests
import time
import sys
import re
import concurrent.futures
import threading
import itertools
user_input = input('Please enter a product type. For example: keyboards, headphones, displays, etc. \n')


done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!')

t = threading.Thread(target=animate)
t.start()



try:
    url = f'https://desktop.bg/{user_input}-all'
    results = requests.get(url).text
    doc = BeautifulSoup(results, 'html.parser')
    page_number = int(doc.find(class_='pagination').find_all('a')[-2].text)
except Exception:
    print(f'Not existing url address {url}, Please restart the script cuz im too lazy to make a while loop :)')
    quit()
all_products = {}
def extract_page_info(curr_page_n):
    all_page_products = {}
    url = f'https://desktop.bg/{user_input}-all?page={curr_page_n}'
    page = requests.get(url).text
    doc = BeautifulSoup(page, 'html.parser')
    products = doc.find(class_='products').contents

    for i in range(len(products)):
        try:
            if doc.find(class_='products').contents[i] == '\n':
                continue
            name = doc.find(class_='products').contents[i].a['title']
            price = doc.find(class_='products').contents[i].find(class_='price').text[:-3]
            link = doc.find(class_='products').contents[i].a['href']
            all_products[name] = [int(price), link]

        except Exception:
            pass



with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(extract_page_info, curr_page_n) for curr_page_n in range(1, page_number+1)]
all_products_sorted = {k: v for k, v in sorted(all_products.items(), key=lambda item: item[1])}
for k, v in all_products_sorted.items():
    print(f'''    {k}
    price: {v[0]}лв.
    link: {v[1]} 
    -----------------------------
''')
done = True





