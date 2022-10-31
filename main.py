from bs4 import BeautifulSoup
import requests


def get_product_info():

    product_name = ''
    price = ''
    product_info = {}
    price_str = ''
    flag = 0
    product_url = 'https://desktop.bg/keyboards-razer-RZ03_03390200R3M1?utm_source=desktop.bg&utm_medium=listing+banner&utm_campaign=razer+huntsman+mini'
    result = requests.get(product_url)
    doc = BeautifulSoup(result.text, 'html.parser')
    prices = (doc.find_all('meta'))
    doc_price = prices[20].find_all('script')[0].string
    print(doc_price)
    doc_price_splited = doc_price.split(' ')
    print(doc_price_splited)
    for i in range(len(doc_price_splited)):
        j = 0
        if "\'fb_product_price\':" in doc_price_splited[i]:
            price_str = doc_price_splited[i+1]
            price = f'{price_str[1:-2]} лв'
            flag = 1
        if "\'fb_product_name\'" in doc_price_splited[i]:
            while "\n" not in product_name:

                product_name += f' {doc_price_splited[(i+1)+j]}'
                j += 1
                flag = 1
        if flag == 1:
            product_info[product_name] = price
            flag = 0
    return product_info


print(get_product_info().items())



