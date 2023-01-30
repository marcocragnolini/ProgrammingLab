class Automobile():
    def __init__ (self,casa_auto,modello,numero_posti,targa):
        self.casa_auto = casa_auto
        self.modello = modello
        self.numero_posti = numero_posti
        self.targa = targa
    def __str__ (self):
        print ('Auto: {} {}, {} posti, {}'.format(self.casa_auto,self.modello,self.numero_posti,self.targa))
        print ('Casa Automobilistica: {}'.format(self.casa_auto))
        print ('Modello: {}'.format(self.modello))
        print ('Numero di posti: {}'.format(self.numero_posti))
        print ('Targa: {}'.format(self.targa))
    def parla ():
        print ('Broom Broom')
    def confronta (auto1,auto2):
        if auto1.casa_auto == auto2.casa_auto and auto2.modello == auto1.modello and auto1.numero_posti == auto2.numero_posti:
            return True
        else: 
            return False

Auto1 = Automobile('Mercedes','Serie S','5','GF045HZ')
Auto2 = Automobile('Mercedes','Serie C','5','FA327HY')
Auto1.__str__()
Auto2.__str__()
if Auto1.confronta(Auto2):
    print ('Le due auto sono uguali')
else:
    print ('Le due auto sono diverse')
