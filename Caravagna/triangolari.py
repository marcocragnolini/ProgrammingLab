class Triangolari ():
    def __init__ (self, n):
        self.n = n
        self.a = 1
        self.counter = 0
    def __iter__ (self):
        return self
    def __next__ (self):
        while True:
            if self.counter < self.n:
                if self.triangolare(self.a):
                    x = self.a
                    self.a += 1
                    self.counter += 1
                    return x
                else:
                    self.a += 1
            else:
                raise StopIteration
    def triangolare (self, x):
        sum = 0
        for i in range (x):
            sum += i
            if sum==x:
                return True
        return False


numero_triangolare = Triangolari(10)
iterable = iter(numero_triangolare)

for x in iterable:
    print (x)
            