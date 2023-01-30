class CSVFile():
    def __init__ (self, name):
        try:
            self.name = name
        except OSError as o:
            print ("Errore:{}".format(o))
    def get_data (self):
        try:
            my_file = open(self.name)
            my_list = []
            for line in my_file:
                elements = line.split(',')
                if elements[0] != 'Date':
                    try:
                        num = float(elements[1])
                        my_list.append(num)
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


class NumericalCSVFile (CSVFile):
    def __init__ (self, name):
        self.name = name
    def original_get_data (self):
        super().get_data()
    def sum (self):
        list = super().get_data()
        sum = 0
        for item in list:
            sum = sum + item
        return sum
        
        
    
file = NumericalCSVFile('shampoo_sales.csv')
print (file.name)
sum = file.sum()
print (sum)


