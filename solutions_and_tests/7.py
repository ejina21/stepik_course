n = int(input())
my_dict = {}
flag = 0


def get_keys(my_dict, el, k, pop=None):
    if pop is None:
        pop = {}
    global flag
    keys = my_dict.keys()
    for key in keys:
        if key == k:
            pop = my_dict.get(k)
        if key == el:
            my_dict[el][k] = pop
            flag = 1
            return 1
        else:
            get_keys(my_dict[key], el, k, pop)
    return 0


dict_lst = {}
for _ in range(n):
    a = input().split(' : ')
    if len(a) > 1:
        b = a[1].split()
        dict_lst[a[0]] = []
        for el in b:
            get_keys(my_dict, el, a[0])
            if flag == 0:
                my_dict[el] = {a[0]: {}}
            flag = 1
            dict_lst[a[0]].append(el)
    else:
        dict_lst[a[0]] = []
        my_dict[a[0]] = {}

for key in dict_lst.keys():
    for elem in dict_lst[key]:
        if elem in dict_lst.keys():
            for item in dict_lst[elem]:
                dict_lst[key].append(item)

q = int(input())
for _ in range(q):
    pred, child = input().split()
    if child in dict_lst.keys() and (pred in dict_lst[child] or pred == child):
        print('Yes')
    else:
        print('No')