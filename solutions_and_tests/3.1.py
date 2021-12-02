stroka = input()
search = input()
change = input()
flag = True
for i in range(1000):
    if search in stroka:
        stroka = stroka.replace(search, change)
    else:
        flag = False
        print(i)
        break
if flag:
    print('Impossible')