class CSVFile ():
    def __init__ (self, name):
        try:
            self.name = name
            file = open (self.name, 'r')
            file.readline()
            file.close()
        except TypeError as t:
            raise Errore ("Errore: {}".format(t))
        except ValueError as v:
            raise Errore("Errore: {}".format(v))
        except OSError as o:
            raise Errore("Errore: {}".format(o))
        except Exception as e:
            raise Errore("Errore: {}".format(e))
        
        
    def get_data (self, start = None, end = None):
        try:
            my_file = open (self.name, 'r')
            my_file.readline()
            my_file.close()
            my_file = open (self.name, 'r')
            data = []
            self.number_lines = 0
            if not my_file:
                data = None
                return data
            for line in my_file:
                self.number_lines = self.number_lines + 1
            if start is None:
                start = 1
            if end is None:
                end = self.number_lines
            try:
                start = int(start)
            except Exception as e:
                raise Errore("Errore: {}".format(e))
            try: 
                end = int(end)
            except Exception as e:
                print ("Errore: {}".format(e))
                raise Errore("Errore")
            if end < start or end > self.number_lines or start < 1 or end < 1 or start > self.number_lines:
                print ("Errore")
                raise Errore ("Errore. Inizio e/o Fine inseriti non sono validi")
            self.counter = 1
            for line in my_file:
                if self.counter == 1:
                    pass
                if self.counter < start:
                    pass
                if self.counter >= start and self.counter <= end:
                    cleaned_line = line.strip('\n')
                    data.append(cleaned_line)
                if self.counter > end:
                    return data
                self.counter = self.counter + 1
        except Exception as e:
            print ("Errore: {}".format(e))
            raise Errore ('Errore')
            return None

class NumericalCSVFile (CSVFile):
    def __init__ (self,name):
        self.name = name
    def get_data(self,*args,**kwargs):
        csv_data = super().get_data(*args, **kwargs)
        return csv_data
        

class Errore(Exception):
    def __init__ (self, name):
        self.name = name
    pass


my_file = NumericalCSVFile ('empty_file.txt')
my_data = my_file.get_data()
print (my_data)

                    
                
            
            
            
            
            
            
        