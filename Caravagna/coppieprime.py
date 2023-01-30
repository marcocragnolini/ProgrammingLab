class CoppiePrime ():
    def __init__ (self, n):
        self.n = n
        self.numero = 1
        self.counter = 0
    def __iter__ (self):
        return self
    def __next__ (self):
        while True:
            if self.counter < self.n:
                if self.primo(self.numero) and self.primo(self.numero+2):
                    x = self.numero
                    self.numero += 1
                    self.counter += 1
                    return x
                else:
                    self.numero += 1
            else:
                raise StopIteration
    def primo (self, x):
        for i in range (2,x):
            if (x%i == 0):
                return False
            if (i == x - 1):
                return True



coppieprime = CoppiePrime (100)
iterable = iter(coppieprime)

for x in iterable:
    y = x+2
    print ("[{};{}]".format(x,y))
    
            