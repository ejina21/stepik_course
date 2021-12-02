class Buffer:
    def __init__(self):
        self.list = []
        # конструктор без аргументов
    def add(self, *args):
        for arg in args:
            self.list.append(arg)
        while len(self.list) >= 5:
            sum = 0
            for i in range(5):
                sum += self.list.pop(0)
            print(sum)

    def get_current_part(self):
        return self.list
buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]