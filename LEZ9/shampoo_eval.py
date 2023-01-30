class Model ():
    def fit (self,data):
        raise NotImplementedError ("Metodo non implementabile")
    def predict (self, data):
        raise NotImplementedError ("Metodo non implementabile")

class IncrementModel(Model):
    def predict (self,data):
        window = 3
        difference=0
        i=0
        for i in range(0,window-1):
            difference+=data[i+1]-data[i]
            i+=1
            if i==(window-1):
                self.predictive_value = data[i]+(difference/(window-1))
        return self.predictive_value
    def evaluate (self):
        self.errors = 0
        data = self.get_data()
        data_2 = []
        for i in range(25,33):
            data_2= [data[i],data[i+1],data[i+2]]
            predictive_value = self.predict(data_2)
            diff = data[i+3] - predictive_value
            if diff < 0:
                diff = -diff
            self.errors+=diff
        return self.errors/10   
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
            
            
                


values = IncrementModel()
value = values.evaluate()
print(value)

class Error ():
    pass