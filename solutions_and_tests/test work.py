class my_list(list):
    def clear(self) -> None:
        print(self.__class__)

l = my_list()
l.clear()
print(my_list)