from bs4 import BeautifulSoup
import requests
import urllib3

def parse():
    urllib3.disable_warnings()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.60'
    }
    url = 'https://auto.drom.ru/all/#tabs'  # ссылка
    page = requests.get(url, headers=headers, verify=False)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    link = soup.findAll('a', {'class':'css-4zflqt e1huvdhj1'})
    title = soup.findAll('div', {'data-ftid': 'bull_title'})
    i=1
    file = open("parsed.txt", 'w')
    for data in title:
        a=data.text
        file.write(a + " - ")
        href= link[i-1].get('href')
        file.write(href + "/n")
        i+=1
    file.close()
    print("Файл создан.")

parse()