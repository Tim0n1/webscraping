import requests
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/accounts/login/'
url_main = url + 'ajax/'
auth = {'username': 'rali.1georgieva', 'password': 'shadowhex06'}
headers = {'referer': "https://www.instagram.com/accounts/login/"}
soup = BeautifulSoup(requests.get(url).text, "html.parser")
csrf = soup.find(name="csrf")
print(csrf)

with requests.Session() as s:
    req = s.get(url)
    r = s.post(url_main, data=auth, headers=headers)
    # Now, you can use 's' object to 'get' response from any instagram url
    # as a logged in user.
    print(r.text)
    #r = s.get('https://www.instagram.com/accounts/edit/')
    # If you want to check whether you're getting the correct response,
    # you can use this:
