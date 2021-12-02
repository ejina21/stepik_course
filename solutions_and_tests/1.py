objects = [0, 1, True, False, 3]
ans = set()
for obj in objects:
    ans.add(id(obj))

print(len(ans))