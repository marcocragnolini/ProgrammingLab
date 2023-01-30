class Model ():
    def __init__ (self, name, length):
        self.name = name
        self.length = length
    def predict (self, data):
        if isinstance (data, list):
            pass
        else:
            raise Error("Errore. Non mi è stata fornita una lista")
        prev_value = None
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
        prev_value = last_value + medium_increment
        return prev_value

data = 31
values = Model('Predizione Vendite', 3)
print (values.name)
predictive_value = values.predict(data)
print (predictive_value)

    
class Error():
    pass

        
            