class Pari():
    def __init__ (self, n):
        self.n = n
        self.a = 0
        self.counter = 0
    def __iter__ (self):
        return self
    def __next__ (self):
        while True:
            if self.counter < self.n:
                if self.a%2==0:
                    x = self.a
                    self.a += 1
                    self.counter += 1
                    return x
                else:
                    self.a += 1
            else:
                raise StopIteration

pari = Pari(20)
mieipari = iter(pari)
for item in mieipari:
    print (item)