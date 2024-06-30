class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= 0:
            if self.start < 0 or self.end < 0:
                print('Пожалуйста, введите значения от нуля и выше')
                raise StopIteration
            if self.i == self.start:
                self.start += 1
            if (self.start % 2) != 0:
                self.start += 1
            if (self.start % 2) == 0:
                self.i = self.start
                if self.start > self.end:
                    raise StopIteration
                return self.start


en = EvenNumbers(10, 25)
for i in en:
    print(i)
