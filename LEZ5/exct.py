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
                    my_list.append(elements)
            return my_list
        except OSError as o:
            print ("Errore: {}".format(o))