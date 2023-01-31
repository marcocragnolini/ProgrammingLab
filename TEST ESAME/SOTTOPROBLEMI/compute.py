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

def diff_maxmin (numeric_list):
    min = numeric_list[0] #assumo che il minimo sia il primo valore
    max = numeric_list[0] #assumo anche che il massimo sia il primo valore
    for i in range(1,len(numeric_list)):
        if numeric_list[i] >= max: 
            max = numeric_list[i]
        if numeric_list[i] <= min:
            min = numeric_list[i]
    if max!=min: #se massimo e minimo sono diversi significa che ci sono almeno due valori...
        return max-min
    else: #...altrimenti ce n'è solo uno e devo tornare None
        return None
            
def compute_daily_max_difference (time_series):
    current = time_series[0] #assegno a tmp la prima sottolista della lista time_series
    previous_timestamp = current[0]
    current_day = current[0]-(current[0]%86400) #creo una variabile che contenga il l'inizio del giorno corrente, inizialmente il primo
    last = time_series[len(time_series)-1] #creo una lista che contenga l'ultima sottolista della lista time_series
    last_day = last[0] - (last[0]%86400) #creo una variabile che contenga l'inizio dell'ultimo giorno della lista time_series
    second_last = time_series[len(time_series)-2] #creo una lista che contenga la penultima sottolista della lista time_series
    second_last_day = second_last[0] - (second_last[0]%86400) #creo una variabile che contenga l'inizio del giorno della penultima lista
    diff_list = [] #creo una lista che conterrà le differenze massime di ogni giornata
    tmp_list = [] #creo una lista temporanea che passerò a una funzione di supporto che me ne calcola differenza massima
    counter = 1 #creo un contatore che tenga traccia di dove sono nella lista
    for item in time_series: #per ogni sottolista (item) di time_series
        if previous_timestamp == item[0] and counter > 1:
            raise ExamException ('Errore: ci sono due timestamp consecutivi uguali')
        else:
            previous_timestamp = item[0]
        if item[0] < (current_day + 86400) and (item[0] >= current_day): #se il timestamp appartiene al giorno in questione...
            tmp_list.append(item[1]) #...aggiungo la temperatura alla lista temporanea
            counter = counter + 1
        if item[0] < current_day or item[0] >= (current_day+172800): #se c'è un timestamp fuori posto, quindi se precede il giorno corrente o se salta un giorno...
            raise ExamException ("Errore: c'è un timestamp fuori posto") #...alzo un'eccezione
        if (item[0] >= (current_day + 86400) and item[0] < (current_day+172800)) or (current_day == last_day and counter == len(time_series) + 1): #se il timestamp appartiene al giorno successivo o sono all'ultimo giorno e all'ultimo valore...
            diff_list.append(diff_maxmin(tmp_list)) #passo lista temporanea a funzione che calcola differenza massima e aggiungo il risultato alla lista che dovrò ritornare
            current_day = current_day + 86400 #passo al giorno successivo
            counter = counter + 1
            tmp_list = [item[1]] #istanzio la lista alla temperatura corrente; se instanziassi a vuota salterei ogni volta un valore 
            if current_day == last_day and second_last_day!=last_day: #se l'ultimo e il penultimo giorno non corrispondono significa che l'ultimo è un valore isolato, quindi devo gestirlo a parte
                diff_list.append(diff_maxmin(tmp_list))
    return diff_list
            
        
            
            
class ExamException (Exception):
    pass

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
diff = compute_daily_max_difference(time_series)
for item in diff:
    print(item)