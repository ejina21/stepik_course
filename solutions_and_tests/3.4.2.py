def rec(my_dict, my_list, my_key):
    while len(my_list) > 0:
        for elem in my_list:
            val = my_dict[elem]
            for v in val:
                my_dict[my_key].append(v)
            rec(my_dict, val, my_key)
        break

import json
a = json.loads(input())
my_dict = {}
for elem in a:
   my_dict[elem['name']] = elem['parents']

for key in my_dict:
    rec(my_dict, my_dict[key], key)

finish = {}
for k in my_dict:
    count = 1
    for key in my_dict:
        if k in my_dict[key]:
            count += 1
    finish[k] = count

sort = sorted(finish.items(), key=lambda x: x[0])
finish = dict(sort)
for key in finish:
    print(key + ' : ' + str(finish[key]))