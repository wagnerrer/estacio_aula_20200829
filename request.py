import requests
from bs4 import BeautifulSoup

cookies = {
    'geoC': 'BR',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept-Language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
}

params = (
    ('timeframe', '300'),
)

response = requests.get('https://ssltsw.forexprostools.com/index.php', headers=headers, params=params, cookies=cookies)
#print(response.text)

active = 'EUR/USD'

soup = BeautifulSoup(response.text)
print(soup.find(id="summaryName").text)
print(soup.find(id="summaryLast").text)
print(soup.find(id="summaryChange").text)
print(soup.find(id="updateTime").text)
print(soup.find(id="technicalSummary").text)

result = {
    'active': active
}
for tr in soup.find_all('tr'):
    td = tr.find_all('td')
    if td[2].text == active:
        result['price'] = td[3].text
        result['sinal'] = td[4].text

print(result)