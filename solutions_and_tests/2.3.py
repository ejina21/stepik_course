class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError

lst = PositiveList()
lst.append(5)
print(lst)
lst.append(0)
print(lst)