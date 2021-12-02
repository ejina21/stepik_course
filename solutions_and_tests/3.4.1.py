import csv
from collections import Counter

with open("../files_from_course/Crimes.csv") as f:
    reader = csv.DictReader(f)
    list = []
    for row in reader:
        list.append(row['Primary Type'])
    c = Counter(list)
    print(c)

