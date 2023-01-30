class Viaggio ():
    def __init__ (self, name):
        self.name = name 
    def quando (self):
        self.data_partenza = []
        print ("Quando vuoi partire?")
        giorno_partenza = input ("Giorno: \n")
        self.data_partenza.append(int(giorno_partenza))
        mese_partenza = input ("Mese: \n")
        self.data_partenza.append(int(mese_partenza))
        self.data_ritorno = []
        print ("Quando vuoi ritornare?")
        giorno_ritorno = input ("Giorno: \n")
        self.data_ritorno.append(int(giorno_ritorno))
        mese_ritorno = input ("Mese: \n")
        self.data_ritorno.append(int(mese_ritorno))
    def dove (self):
        self.località = input ("Dove vuoi andare? \n")
    def prezzo (self):
        pass
    def partecipanti (self):
        partecipanti = input("Inserisci i partecipanti, separando i cognomi con una virgola: \n")
        self.partecipanti = []
        self.partecipanti = partecipanti.split(',')
        self.numero_partecipanti = len(self.partecipanti)
    def resort (self):
        stelle = input ("Quante stelle deve avere il resort/hotel? Sappi che mediamente i prezzi a notte sono: \n75 euro per 5 stelle\n60 euro per 4 stelle\n45 euro per 3 stelle\n30 euro per 2 stelle\n15 euro per 1 stella\nStelle: ")
        self.stelle = int(stelle)
    def responsabile_viaggio (self, responsabile_viaggio):
        self.responsabile_viaggio = responsabile_viaggio
    def stampa (self,responsabile_viaggio):
        self.dove()
        self.quando()
        self.partecipanti()
        self.responsabile_viaggio(responsabile_viaggio)
        self.resort()
        
        self.prezzo (self.numero_partecipanti)
        print ("\n\n")
        print ("La località è {}".format(self.località))
        print ("La partenza è il giorno: {}".format(self.data_partenza))
        print ("Il ritorno è il giorno: {}".format(self.data_ritorno))
        if self.stelle == 1:
            print ("L'hotel/resort è a {} stella".format(self.stelle))
        else:
            print ("L'hotel/resort è a {} stelle".format(self.stelle))
        if self.estate == True:
            self.distanza()
            print (self.distanza)
        print ("I partecipanti sono:")
        for item in self.partecipanti:
            print (item)
        print ("Prezzo a partecipante")
        for item in self.costo_a_partecipante:
            print (item)
        print ("Il prezzo totale è: {}".format(self.prezzo_totale))
        print ("Il responsabile viaggio è {}".format(self.responsabile_viaggio))

class ViaggioInvernale ():
    def __init__ (self):
        self.estate = False
    def prezzo (self, numero_partecipanti):
        numero_skipass = input ("Quanti partecipanti vogliono lo skipass?")
        self.prezzo_a_notte = self.stelle * 15
        self.costo_a_partecipante = []
        for i in range (numero_partecipanti):
            self.costo_a_partecipante.append(self.prezzo_a_notte)
        if self.località == 'Saint Moritz':
            for i in range (numero_skipass):
                self.costo_a_partecipante[i] = self.costo_a_partecipante[i] * 1.10
        if self.località == 'Cortina':
            for i in range (numero_skipass):
                self.costo_a_partecipante[i] = self.costo_a_partecipante[i] * 1.15
        else:
            for i in range (numero_skipass):
                self.costo_a_partecipante[i] = self.costo_a_partecipante[i] * 1.05
        self.impianti_sciistici = ['Pista 1', 'Pista 2', 'Impianto Snowboard', 'Palazzetto', 'Impianto Sportivo']
        self.prezzo_totale = 0
        for item in self.costo_a_partecipante:
            self.prezzo_totale = self.prezzo_totale + item

class ViaggioEstivo(Viaggio):
    def __init__ (self):
        self.estate = True
    def distanza (self):
        self.distanza = 1000/self.stelle
    def prezzo(self, numero_partecipanti):
        self.numero_giorni = self.data_ritorno[0] - self.data_partenza[0]
        self.costo_a_partecipante = []
        self.costo_a_notte = self.stelle*15
        for item in self.costo_a_partecipante:
        
        self.prezzo_totale = self.costo_a_notte * numero_giorni
        
    
        
            
            
        
        

    
        
        
    
        
    
    




viaggio = ViaggioEstivo()
viaggio.stampa('Marco Cragnolini')