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
                    except TypeError as t:
                        print ("Errore: {}".format(t))
                    except ValueError as v:
                        print ("Errore: {}".format(v))
                    my_list.append(num)
            return my_list
        except OSError as o:
            print ("Errore: {}".format(o))
        
    
    
file = CSVFile()
print (file.name)
print (file.get_data())