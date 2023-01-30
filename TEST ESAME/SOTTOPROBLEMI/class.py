class CSVFile ():
    def __init__ (self,name):
        self.name = name
    def get_data(self):
        raise NotImplementedError ('Errore. Funzione non implementata')


class CSVTimeSeriesFile (CSVFile):
    def __init__ (self,name):
        self.name = name
    def get_data(self):
        try:
            time_series_test = open(self.name, 'r') #provo ad aprire il file in una variabile di test
            time_series_test.readline() #provo a leggerne una riga
            time_series_file = open(self.name, 'r') #provo finalmente ad aprire il file nella variabile che mi serve
        except OSError as o:
            raise ExamException ('Errore: {}'.format(o))
        except TypeError as t:
            raise ExamException ('Errore: {}'.format(t))
        except Exception as e:
            raise ExamException ('Errore: {}'.format(e))
        time_series_list = [] #creo una lista vuota a cui aggiungerò il contenuto "pulito" delle righe del file 
        for line in time_series_file:
            cleaned_line = line.strip('\n') #ripulisco la riga dal carattere speciale \n
            elements = cleaned_line.split(',') #divido alla virgola così da separare i due elementi
            #if elements[0] != 'epoch': #se non sono nell'intestazione
            try: #provo a trasformare gli elementi della riga in numerici per poterli utilizzare dopo
                elements[0] = int(elements[0]) #il timestamp in intero (float non ha senso)
                elements[1] = float(elements[1]) #la temperatura in float (se no approssimo)
            except ValueError:
                continue
            except TypeError:
                continue
            except Exception:
                continue
            time_series_list.append(elements) #aggiungo la lista elements alla lista che dovrò ritornare
        if len(time_series_list) == 0: #controllo che il file non fosse vuoto verificando che non mi abbia creato una lista vuota
            raise ExamException ('Errore: il file ha creato una lista vuota')
        if time_series_list is None: #controllo che la lista non sia None anche se è improbabile
            raise ExamException ('Errore: la lista è None')
        return time_series_list
            
        
        





class ExamException (Exception):
    pass

time_series_file = CSVTimeSeriesFile('datatest.csv')
time_series = time_series_file.get_data()
print(time_series)