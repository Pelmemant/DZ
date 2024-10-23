class StepValueError(ValueError):
    def __init__(self, message):
        super().__init__(message)


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if step == 0:
            raise StepValueError('Шаг указан неверно')
        self.pointer = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer <= self.stop:
            self.pointer += self.step
            return self.pointer
        else:
            raise StopIteration


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as err:
    print(err)


iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
    print()
for i in iter3:
    print(i, end=' ')
    print()
for i in iter4:
    print(i, end=' ')
    print()
for i in iter5:
    print(i, end=' ')
    print()
