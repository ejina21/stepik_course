import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, *args, **kwargs) -> None:
        super().append(*args)
        self.log(args[0])

lst = LoggableList()
lst.append(13)
print(lst)