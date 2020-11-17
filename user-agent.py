import time

import requests as req
from bs4 import BeautifulSoup

url = 'http://www.useragentstring.com/pages/useragentstring.php?name=Firefox'


def save(br, list):
    file = br + '.txt'

    with open(file, 'w') as f:
        for item in list:
            f.write("%s\n" % item)


def getUa(br):
    url = 'http://www.useragentstring.com/pages/useragentstring.php?name=' + br
    r = req.get(url)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
    else:
        soup = False

    if soup:
        div = soup.find('div', {'id': 'liste'})
        lnk = div.findAll('a')

        for_save = []
        for i in lnk:
            for_save.append(i.text)
            # save(br, i.text)
        print(for_save)
        save(br, for_save)
    else:
        print('No soup for ' + br)


lst = ['Firefox', 'Opera', 'Safari', 'Chrome', 'Edge', 'Android+Webkit+Browser']

for i in lst:
    getUa(i)
    time.sleep(5)
