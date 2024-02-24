class CloneRange:
    def __init__(self, start, stop: None, step = 1):
        if stop is None:
            self.stop = start
            self.start = 0
        self.start = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start >= self.stop:
            raise StopIteration
        return self.start

for i in CloneRange(2,10):
    print(i)