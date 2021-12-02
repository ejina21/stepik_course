stroka = input()
search = input()

index = 0
count = 0
while index < len(stroka):
    if stroka.find(search, index) == -1:
        break
    index = stroka.find(search, index) + 1
    count += 1
print(count)

