n = int(input())
i = 0
dic = {"global": []}


def get_dict(dic, arg):
    if arg in dic.keys():
        return dic

    for k in dic.values():
        for value in k:
            if type(value) is dict:
                my_d = get_dict(value, arg)
                if not my_d is None:
                    return my_d


def root(dic, child):
    for values in dic.values():
        for value in values:
            if type(value) is dict:
                if child in value.keys():
                    for key in dic.keys():
                        return key
                else:
                    my = root(value, child)
                    if not my is None:
                        return my

def get_root(dic, namespace, arg):
    if namespace == "global":
        if arg in dic[namespace]:
            return namespace
        else:
            return None
    my_d = get_dict(dic, namespace)
    for values in my_d.values():
        if arg in values:
            return namespace

    for values in dic.values():
        for value in values:
            if type(value) is dict:
                out = get_root(dic, root(dic, namespace), arg)
                if not out is None:
                    return out


while i < n:
    cmd, namesp, arg = input().split()
    if cmd == "create":
        my_dict = get_dict(dic, arg)
        my_dict[arg].append({namesp: []})
    elif cmd == "add":
        my_dict = get_dict(dic, namesp)
        my_dict[namesp].append(arg)
    elif cmd == "get":
        print(get_root(dic, namesp, arg))
    i += 1
