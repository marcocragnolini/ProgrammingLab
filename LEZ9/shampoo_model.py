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
    def get_data (self):
        try:
            my_file = open(self.name, 'r')
            my_list = []
            for line in my_file:
                elements = line.split(',')
            if elements[0] != 'Date':
                for item in elements:
                    
                    try:
                        my_list.append(float(elements[1]))
                    except TypeError as t:
                        print ("Errore: {}".format(t))
                    except ValueError as v:
                        print ("Errore: {}".format(v))
                    except Exception as e:
                        print ("Errore: {}".format(e))
            print(my_list)
            return (my_list)
        except OSError as o:
            print ("Errore: {}".format(o))
    def fit (self,my_list):
        if isinstance (my_list, list):
            pass
        else:
            raise Error("Errore. Non mi è stata fornita una lista")
        self.precedent_value = None
        self.number_of_values = 0
        local_increment = None
        for item in my_list:
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


data = FitIncrementModel('shampoo_sales.csv')
print ('Modello Predittivo del File: {}'.format(data.name))
my_list = data.get_data()
data.fit(my_list)
print ("Incremento Totale: {}".format(data.global_avg_increment))
data.predict()
print ("Incremento Medio: {}".format(data.medium_increment))
print ("Valore Predittivo: {}".format(data.predictive_value))
#global_avg_increment = values.fit(data)
#predictive_value = values.predict(global_avg_increment)
#print (predictive_value)
