class Model ():
    def __init__ (self, name):
        self.name = name
        self.global_avg_increment = 0
        
    def predict (self, data):
        if isinstance (data, list):
            pass
        else:
            raise Error("Errore. Non mi è stata fornita una lista")
        self.prec_value = None
        self.number_of_values = 0
        local_increment = None
        for item in data:
            if self.number_of_values == 0:
                self.prec_value = item
                pass
            if self.number_of_values > 0:
                local_increment = item - self.prec_value
                self.global_avg_increment = self.global_avg_increment + local_increment
                self.prec_value = item
            self.number_of_values = self.number_of_values + 1
        medium_increment = self.global_avg_increment/(self.number_of_values-1)
        predictive_value = self.prec_value + medium_increment
        return predictive_value
        
            
            
                
        

data = [50,52,60]
values = Model('Predizione Vendite')
print (values.name)
predictive_value = values.predict(data)
print (predictive_value)

    
class Error():
    pass

        
            