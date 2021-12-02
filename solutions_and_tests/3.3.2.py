import lxml.html
import requests
import re

a = input()
res = requests.get(a)

pattern = '(?:.://)?([^/|\.]+\.[a-zA-Z\d]+[^/|:|\?]+)'
pattern2 = '(\.\..*)'
list_links = []
# try:
html = lxml.html.document_fromstring(res.text)
for a in html.iter('a'):
    if a.get('href'):
        if re.search(pattern2, a.get('href')):
            continue
        result = re.findall(pattern, a.get('href'))
        if result:
            list_links.append(result[0])
list_links = list(set(list_links))
list_links.sort()

for i in list_links:
    print(i)
# except Exception:
#     exit()
