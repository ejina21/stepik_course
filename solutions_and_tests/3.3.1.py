import lxml.html
import requests
a = input()
b = input()
res = requests.get(a)

list_links = []
try:
    html = lxml.html.document_fromstring(res.text)
    for a in html.iter('a'):
        l = requests.get(a.get('href'))
        html = lxml.html.document_fromstring(l.text)
        for lin in html.iter('a'):
            if lin.get('href') == b:
                print('Yes')
                exit()
    print('No')
except Exception:
    print('No')
