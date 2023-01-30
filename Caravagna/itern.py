class Primi:
    def __init__ (self, n):
        self.n = n
        self.counter = 0
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        while True:
            if self.a == 1 or self.a == 2:
                x = self.a
                self.counter += 1
                self.a += 1
                return x
            if self.counter < self.n:
                if self.primo():
                    x = self.a
                    self.counter += 1
                    self.a += 1
                    return x
                else:
                    self.a += 1
            else:
                raise StopIteration
    def primo (self):
        for i in range(2,self.a):
            if (self.a%i==0):
                return False
            if (i == self.a - 1):
                return True



primi = Primi(20)
iterable = iter(primi)

for x in iterable:
    print(x)