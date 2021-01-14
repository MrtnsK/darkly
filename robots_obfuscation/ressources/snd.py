import requests
from bs4 import BeautifulSoup
from time import sleep

fdp=set()

baseurl = 'http://192.168.1.97/.hidden/'
def parse(url, baseurl = ""):
    tmp = []
    try:
        page = requests.get(baseurl+url)
    except:
        print("Retry in 10s\n", baseurl+url)
        sleep(10)
        return parse(url, baseurl)
    soup = BeautifulSoup(page.content, "html.parser")
    tmp  = [link.get('href') for link in soup.find_all('a')]
    if "../" in tmp:
        tmp.remove("../")
    if url.endswith("README"):
        fdp.add(page.text)
    return tmp


try:
    tmp = parse(baseurl)
    for elem in tmp:
        tmp2 = parse(elem, baseurl)
        for elem2 in tmp2:
            tmp3 = parse(elem2, baseurl+elem)
            for elem3 in tmp3:
                tmp4 = parse(elem3, baseurl+elem+elem2)
                for elem4 in tmp4:
                    tmp5 = parse(elem4, baseurl+elem+elem2+elem3)
except:
    pass
finally:
    print(fdp)