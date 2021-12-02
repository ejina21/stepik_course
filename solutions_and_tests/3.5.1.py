import requests

with open('../files_from_course/file3.5.1.txt') as f:
    while number := f.readline():
        number = number.strip()
        api_url = f"http://numbersapi.com/{number}/math?json=true"
        res = requests.get(api_url)
        my_dict = res.json()
        if not my_dict['found']:
            print('Boring')
        else:
            print('Interesting')