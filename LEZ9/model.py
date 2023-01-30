class Model ():
    def fit (self,data):
        raise NotImplementedError ("Metodo non implementabile")
    def predict (self, data):
        raise NotImplementedError ("Metodo non implementabile")

class IncrementModel (Model):
    def __init__ (self,name,length):
        self.name = name
        self.length = length
    def predict (self,data):
        if isinstance (data, list):
            pass
        else:
            raise Error("Errore. Non mi è stata fornita una lista")
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
    def fit (self,data):
        super().predict(data)
    
    

class FitIncrementModel (IncrementModel):
    def __init__ (self, name):
        self.name = name
        self.global_avg_increment = 0
    def fit (self, data):
        if isinstance (data, list):
            pass
        else:
            raise Error("Errore. Non mi è stata fornita una lista")
        self.precedent_value = None
        self.number_of_values = 0
        local_increment = None
        for item in data:
            if self.number_of_values == 0:
                self.precedent_value = item
                pass
            if self.number_of_values > 0:
                local_increment = item - self.precedent_value
                self.global_avg_increment = self.global_avg_increment + local_increment
                self.precedent_value = item
            self.number_of_values = self.number_of_values + 1
        return self.global_avg_increment
    def predict (self):
        self.medium_increment = self.global_avg_increment/(self.number_of_values-1)
        self.predictive_value = self.medium_increment + self.precedent_value
        return self.predictive_value

    

class Error ():
    pass

class NotImplementedError (Error):
    pass

data = [8,19,31,41,50,52,60]
values = FitIncrementModel('Modello Predittivo Fittato')
print (values.name)
values.fit(data)
print ("Incremento Totale: {}".format(values.global_avg_increment))
values.predict()
print ("Incremento Medio: {}".format(values.medium_increment))
print ("Valore Predittivo: {}".format(values.predictive_value))
#global_avg_increment = values.fit(data)
#predictive_value = values.predict(global_avg_increment)
#print (predictive_value)
