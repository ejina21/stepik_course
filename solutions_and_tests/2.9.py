import os
import re

with open('../files_from_course/test_2.9.txt', 'w') as f:
    lst = []
    for a, b, c in os.walk('../files_from_course/main'):
        for el in c:
            if re.search(r'/*.py', el):
                lst.append(a)
                break
    lst.sort()
    for el in lst:
        f.write(el + '\n')