class Buffer:
    def __init__(self):
        self.lst = []
        self.count = 0

    def add(self, *a):
        for value in a:
            self.lst.append(value)
            self.count += 1
            if self.count == 5:
                summ = 0
                for ls in self.lst:
                    summ += ls
                print(summ)
                self.lst = []
                self.count = 0

    def get_current_part(self):
        return self.lst
