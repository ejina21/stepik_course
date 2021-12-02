n = int(input())

dict_lst = {}
for _ in range(n):
    a = input().split(' : ')
    if len(a) > 1:
        b = a[1].split()
        dict_lst[a[0]] = []
        for el in b:
            dict_lst[a[0]].append(el)
    else:
        dict_lst[a[0]] = []

for key in dict_lst.keys():
    for elem in dict_lst[key]:
        if elem in dict_lst.keys():
            for item in dict_lst[elem]:
                if item not in dict_lst[key]:
                    dict_lst[key].append(item)
print('-------------------------------')
print(dict_lst)
print('-------------------------------')


q = int(input())
lst = []
for _ in range(q):
    pred = input()
    lst.append(pred)

for n in range(len(lst)):
    for el in lst[0:n]:
        if el in dict_lst[lst[n]] or lst[n] in lst[0:n]:
            print(lst[n])
            # lst.pop(n)
            break
