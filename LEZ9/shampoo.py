class Model ():
    def fit (self,data):
        raise NotImplementedError ("Metodo non implementabile. Where://fit; Model//.")
    def predict (self, data):
        raise NotImplementedError ("Metodo non implementabile. Where://predict; Model//.")
                
                

class IncrementModel (Model):
    def __init__ (self,name,length):
        self.name = name
        self.length = length
    def predict (self,data):
        if isinstance (data, list):
            pass
        else:
            raise Error("Errore. Non mi è stata fornita una lista. Where://predict; IncrementModel//.")
        predictive_value = None
        counter = 1
        first_value = None
        last_value = None
        for item in data:
            if counter == 1:
                try:
                    first_value = float(item)
                except Exception as e:
                    raise Error('Errore: {}. Non posso convertire il primo elemento a un numero'.format(e))
            if counter == self.length:
                try:
                    last_value = float(item)
                except Exception as e:
                    raise Error("Errore: {}. Non posso convertire l'ultimo valore a un numero".format(e))
            else:
                pass
            counter = counter + 1
        medium_increment = (last_value - first_value)/(counter-2)
        predictive_value = last_value + medium_increment
        return predictive_value
    
    

class FitIncrementModel (IncrementModel):
    def __init__ (self, name):
        try:
            if isinstance(name, str):
                self.name = name
                self.global_avg_increment = 0
            else:
                raise Error("Il nome non è una stringa")
        except TypeError as t:
            raise Error("Errore, ##TypeError##: {}. Where://__init__; FitIncrementModel//.".format(t))
        except Exception as e:
            raise Error("Errore, ##Exception##: {}. Where://__init__; FitIncrementModel//.".format(e))
    def get_data (self):
        try:
            my_file = open('shampoo_sales.csv', 'r')
            my_list = []
        except TypeError as t:
            raise Error("Errore, ##TypeError##: {}. Where://get_data; FitIncrementModel//.".format(t))
        except Exception as e:
            raise Error("Errore: {}".format(e))
        for line in my_file:
            cleaned_line = line.strip('\n')
            elements = cleaned_line.split(',')
            if elements[0] != 'Date':
                try:
                    element_to_append = float(elements[1])
                except TypeError as t:
                    raise Error ("Errore, ##TypeError##: {}".format(t))
                except ValueError as v:
                    raise Error ("Errore, ##ValueError##: {}. Where://get_data; FitIncrementModel//.".format(v))
                except Exception as e:
                    raise Error("Errore, ##Exception##: {}. Where://get_data; FitIncrementModel//.".format(e))
                my_list.append(element_to_append)
        return my_list
    def fit (self):
        self.data = self.get_data()
        self.precedent_value = None
        self.number_of_values = 0
        local_increment = None
        if self.data is not None:
            for item in self.data:
                if item is not None:
                    if self.number_of_values == 0:
                        self.precedent_value = item
                        pass
                    if self.number_of_values > 0:
                        local_increment = item - self.precedent_value
                        self.global_avg_increment = self.global_avg_increment + local_increment
                        self.precedent_value = item
                    self.number_of_values = self.number_of_values + 1
                else:
                    raise Error("Errore. L'item {} è None. Where://fit; FitIncrementModel//.".format(self.number_of_values+1))
            return self.global_avg_increment
        else:
            raise Error("Errore, self.data è None. Where://fit; FitIncrementModel//.")
    def predict (self):
        self.medium_increment = self.global_avg_increment/(self.number_of_values-1)
        self.predictive_value = self.medium_increment + self.precedent_value
        return self.predictive_value

    

class Error (Exception):
    def print_error (self, name):
        self.name = name
        print (self.name)

class NotImplementedError (Error):
    pass


values = FitIncrementModel('Modello Predittivo Fittato')
print (values.name)
values.fit()
print ("Incremento Totale: {}".format(values.global_avg_increment))
values.predict()
print ("Incremento Medio: {}".format(values.medium_increment))
print ("Valore Predittivo: {}".format(values.predictive_value))
#CONTROLLO
#print ("Lista shampoo sales: {}".format(values.data))


#IGNORA
#global_avg_increment = values.fit(data)
#predictive_value = values.predict(global_avg_increment)
#print (predictive_value)