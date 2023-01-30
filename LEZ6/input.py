class CSVFile:
    def __init__ (self, name):
        self.name = name #attributo nome al file
        self.is_ok_to_open = True #assumo di default che si possa aprire
        
    def get_data (self, start = None, end = None):  #nel caso in cui non mi siano forniti start e end uso None di default, quindi considero tutta la lista 
        try: #se effettivamente posso, l'attributo rimane True
            my_file = open(self.name, 'r') 
            my_file.readline()
        except Exception as e:
            self.is_ok_to_open = False #campio l'attributo a False
            print ('Errore: {}'.format(e))
            raise Errore ('Errore. File impossibile da aprire')
            
        if my_file is None:
            raise Errore ("Errore. File None")
            return None
        if not self.is_ok_to_open: #se non posso aprire il file
            raise Errore ("Errore. File impossibile da aprire")
            return None
        else:
            try:
                my_file = open(self.name, 'r') 
                my_file_shortened = []#creo lista vuota per contenere le righe del file che voglio
                self.number_lines = 0
                for line in my_file:
                    self.number_lines = self.number_lines + 1
                self.counter = 1 #creo contatore inizializzato alla prima riga che segno come 1
                if start is None:
                    start = 1
                if end is None:
                    end = self.number_lines
                if start is not None and end is not None:
                    try: #provo a passare start a float
                        start = int(start)
                    except Exception as e:
                        raise Errore ("Errore. L'inizio non è un numero. Era stato dato il valore: {}. Errore del tipo: {}".format(start, e))
                    try: #provo a passare end a float
                        end = int(end)
                    except Exception as e:
                        raise Errore ("Errore. La fine non è un numero. Era stato dato il valore: {}. Errore del tipo: {}".format(end ,e))
                    if start < 1 or start > self.number_lines:
                        raise Errore("Errore. Sei fuori dal file. Start è inferiore a 1. Il file ha come riga iniziale 1")
                    if end > self.number_lines or end < 1:
                        raise Errore("Errore. Sei fuori dal file. End è superiore a 36. Il file termina alla riga 36")
                    if start > end: #se l'inizio è più grande della fine
                        raise Errore("L'inizio è dopo la fine")
                    for line in my_file: 
                        if self.counter < start: #se sono prima dell'inizio leggo la riga cosicchè la skippi
                            pass
                        if self.counter >= start and self.counter <= end: #se sono nella sezione che mi interessa aggiungo la riga alla lista che ho creato prima
                            cleaned_line = line.strip('\n')
                            my_file_shortened.append(cleaned_line)
                        if self.counter > end: #se sono oltre la fine ritorno la lista
                            return my_file_shortened
                        self.counter = self.counter + 1 #ogni ciclo incremento il contatore  
            except Exception as e:
                    print ("Errore")
                    raise Errore ("Errore: {}".format(e))
                
class Errore(Exception):
    def stampa (self):
        print ("Errore")
    pass

class NumericalCSVFile (CSVFile):
    def __init__ (self, name):
        self.name = name
        self.is_ok_to_open = True
    def original_get_data (self):
        super().get_data()

my_file = NumericalCSVFile ('shampoo_sales.csv')
print (my_file.get_data(start=None, end = None))

