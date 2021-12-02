import requests

# kw = {
#         'client_id': '1e1431178d830b233e62',
#         'client_secret': '91eec50976ebc4215f0310124457059e'
# }
# urls = 'https://api.artsy.net/api/tokens/xapp_token'
# token_res = requests.post(urls, kw)
# print(token_res.json())
xapp_token = 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI2MTZkMTEwNjUwNmY2MjAwMGQ0NDliMzQi' \
             'LCJleHAiOjE2MzUxNDI1MzUsImlhdCI6MTYzNDUzNzczNSwiYXVkIjoiNjE2ZDExMDY1MDZmNjIwMDBkNDQ5YjM0IiwiaXNzIjoiR3J' \
             'hdml0eSIsImp0aSI6IjYxNmQxMTA3ZjAzNjg0MDAwYjEzMDc5OCJ9.5zPJ4QhiNSAZl69YjkP90T4YxNAYV_aHMVS2qt8Tq28'

headers = {"X-Xapp-Token": xapp_token}

my_dict = {}
with open('../files_from_course/file3.5.2.txt') as f:
    while id := f.readline():
        id = id.strip()
        res = requests.get(f"https://api.artsy.net/api/artists/{id}", headers=headers)
        info = res.json()
        my_dict[info['sortable_name']] = info['birthday']

my_list = sorted(my_dict.items(), key=lambda x: (x[1], x[0]))
for item in my_list:
    print(item[0])